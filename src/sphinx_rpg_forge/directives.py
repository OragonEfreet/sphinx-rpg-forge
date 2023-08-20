from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx_rpg_forge.constants import RPG_DOMAIN
from sphinx_rpg_forge.nodes import RuleSetNode
import re


class ForgeObjectDescription(ObjectDescription):
    has_content = False
    required_arguments = 1
    option_spec = {
        "noindex": directives.flag,
        "title": directives.unchanged_required,
    }

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=self.options.get("title", sig))
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode["ids"].append(
            self.env.get_domain(RPG_DOMAIN).add_object("RuleSet", sig)
        )

    def get_object_type():
        return "ForgeObject"


class RuleSetDirective(ForgeObjectDescription):
    def get_object_type():
        return "RuleSet"


class CharacterDirective(ForgeObjectDescription):
    has_content = True

    def get_object_type():
        return "Character"
