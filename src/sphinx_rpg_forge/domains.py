from sphinx.domains import Domain
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode
from sphinx_rpg_forge.constants import RPG_DOMAIN
from sphinx_rpg_forge.directives import *
from sphinx_rpg_forge.forge import *
from sphinx_rpg_forge.indices import *
from sphinx_rpg_forge.roles import *


class ForgeDomain(Domain):

    name = RPG_DOMAIN
    label = 'RPG Forge'

    object_types = []

    directives = {
        'ruleset': RuleSetDirective,
    }
    indices = {
        RuleSetIndex,
    }
    roles = {
        'ruleset': XRefRole(),
        'char': DummyRole(),
        'carac': DummyRole(),
        'roll': DummyRole(),
    }
    initial_data = {
        'objects': [],  # A flat list of all the objects
    }

    def get_full_qualified_name(self, node):
        return f'rpg.forge.{node.arguments[0]}'

    def get_objects(self):
        # TODO
        yield from []
        # yield from self.data['objects']

    def get_rulesets(self):
        for obj in self.data['objects']:
            if obj.typ == 'RuleSet':
                yield obj

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        match typ:
            case 'ruleset':
                for rs in self.get_rulesets():
                    if rs.name == target:
                        return make_refnode(builder, fromdocname, rs.docname, rs.anchor, contnode, rs.docname)

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

    def add_ruleset(self, signature, dispname):
        """Add a new ruleset to the domain
        Returns the name for the ruleset"""
        name = signature
        anchor = f'ruleset-{signature}'
        self.data['objects'].append(
            RuleSet(name, dispname, self.env.docname, anchor))
        return name
