from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx_rpg_forge.constants import RPG_DOMAIN
from sphinx_rpg_forge.nodes import RuleSetNode
import re


class RuleSetDirective(ObjectDescription):
    has_content = False
    required_arguments = 1
    option_spec = {
        "noindex": directives.flag,
    }

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=sig)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode["ids"].append(
            self.env.get_domain(RPG_DOMAIN).add_object("RuleSet", sig)
        )

class CharacterDirective(ObjectDescription):
    has_content = False
    final_argument_whitespace = False
    required_arguments = 1
    option_spec = {
        "noindex": directives.flag,
    }

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=sig)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode["ids"].append(
            self.env.get_domain(RPG_DOMAIN).add_object("Character", sig)
        )
