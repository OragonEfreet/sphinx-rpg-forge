from sphinx.domains import Domain
from sphinx_rpg_forge.directives import *
from sphinx_rpg_forge.roles import *


class ForgeDomain(Domain):

    name = 'rpg'
    label = 'RPG Forge'

    object_types = []

    directives = {
        'ruleset': RuleSetDirective,
    }

    roles = {
        'char': DummyRole(),
        'carac': DummyRole(),
        'roll': DummyRole(),
    }

    initial_data = {}
