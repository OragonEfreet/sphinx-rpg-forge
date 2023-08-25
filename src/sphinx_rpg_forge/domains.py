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
        ForgeIndex,
    }
    roles = {
        "ruleset": XRefRole(),
        "char": XRefRole(),
        "carac": DummyRole(),
        "roll": DummyRole(),
    }
    initial_data = {
        "objects": [],  # A flat list of all the objects
        "current_ruleset": {},
    }

    def get_full_qualified_name(self, node):
        return f"rpg.forge.{node.arguments[0]}"

    def get_objects(self):
        yield from [obj.description() for obj in self.data["objects"]]

    def get(self, objtype):
        yield from [obj for obj in self.data["objects"] if obj.typ == objtype]

    def current_ruleset(self, docname):
        return self.data["current_ruleset"].get(docname, None)

    def set_current_ruleset(self, docname, ruleset):
        self.data["current_ruleset"][docname] = ruleset

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        match typ:
            case "ruleset":
                try:
                    rs = next(
                        rs for rs in self.get(RuleSetDirective.get_object_type()) if rs.signature == target
                    )
                    return rs.make_refnode(builder, fromdocname, contnode)
                except StopIteration:
                    pass
            case "char":
                try:
                    rs = next(
                        rs for rs in self.get(CharacterDirective.get_object_type()) if rs.signature == target
                    )
                    return rs.make_refnode(builder, fromdocname, contnode)
                except StopIteration:
                    pass

            case _:
                return None
        return None

    def add_object(self, typ, signature, ruleset):
        """Add a new object of the given type to the domain
        Returns the anchor to the object"""
        name = f"{typ}.{signature}"
        anchor = f"{typ}-{signature}"
        new_object = ForgeObject(name, signature, typ, self.env.docname, anchor, ruleset)
        self.data["objects"].append(new_object)
        return new_object
