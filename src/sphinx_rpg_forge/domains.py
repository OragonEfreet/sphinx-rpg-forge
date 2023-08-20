from sphinx.domains import Domain
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
        'char': DummyRole(),
        'carac': DummyRole(),
        'roll': DummyRole(),
    }
    initial_data = {
        # An {str: str} dict where they key identified a ruleset and
        # the value is a display name for the ruleset
        'rulesets': [],
    }

    def get_full_qualified_name(self, node):
        return f'rpg.forge.{node.arguments[0]}'

    def get_objects(self):
        # TODO
        yield from []

    def get_rulesets(self):
        yield from self.data['rulesets']

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        # TODO
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
        return None

    def add_ruleset(self, signature, dispname):
        """Add a new ruleset to the domain"""
        name = f'ruleset.{signature}'
        anchor = f'ruleset-{signature}'

        # assert (signature not in self.data['rulesets'])
        self.data['rulesets'].append(
            RuleSet(name, dispname, self.env.docname, anchor))
