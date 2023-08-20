from sphinx.domains import Domain
from sphinx.roles import XRefRole
from sphinx_rpg_forge.constants import RPG_DOMAIN
from sphinx_rpg_forge.directives import *
from sphinx_rpg_forge.forge import *
from sphinx_rpg_forge.indices import *
from sphinx_rpg_forge.roles import *


class ForgeDomain(Domain):
    name = RPG_DOMAIN
    label = "RPG Forge"

    object_types = []

    directives = {
        "ruleset": RuleSetDirective,
        "character": CharacterDirective,
    }
    indices = {
        RuleSetIndex,
    }
    roles = {
        "ruleset": XRefRole(),
        "char": XRefRole(),
        "carac": DummyRole(),
        "roll": DummyRole(),
    }
    initial_data = {
        "objects": [],  # A flat list of all the objects
    }

    def get_full_qualified_name(self, node):
        return f"rpg.forge.{node.arguments[0]}"

    def get_objects(self):
        yield from [obj.description() for obj in self.data["objects"]]

    def get_rulesets(self):
        yield from [obj for obj in self.data["objects"] if obj.typ == "RuleSet"]

    def get_characters(self):
        yield from [obj for obj in self.data["objects"] if obj.typ == "Character"]

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        match typ:
            case "ruleset":
                try:
                    rs = next(
                        rs for rs in self.get_rulesets() if rs.signature == target
                    )
                    return rs.make_refnode(builder, fromdocname, contnode)
                except StopIteration:
                    pass
            case "char":
                try:
                    rs = next(
                        rs for rs in self.get_characters() if rs.signature == target
                    )
                    return rs.make_refnode(builder, fromdocname, contnode)
                except StopIteration:
                    pass

                # print('====== RESOLVE =====')
                # print(f'    self: {self}')
                # print(f'    env: {env}')
                # print(f'    fromdocname: {fromdocname}')
                # print(f'    builder: {builder}')
                # print(f'    typ: {typ}')
                # print(f'    target: {target}')
                # print(f'    node: {node}')
                # print(f'    contnode: {contnode}')
                # print('====================')

            case _:
                return None
        return None

    def add_object(self, typ, signature):
        """Add a new object of the given type to the domain
        Returns the anchor to the object"""
        name = f"{typ}.{signature}"
        anchor = f"{typ}-{signature}"
        self.data["objects"].append(
            ForgeObject(name, signature, typ, self.env.docname, anchor)
        )
        return anchor
