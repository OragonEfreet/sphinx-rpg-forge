from docutils import nodes
from docutils.nodes import Node
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
        "ruleset": directives.unchanged_required,
    }

    def run(self) -> list[Node]:
        nodes = super().run()

        if hasattr(self, 'next_current_ruleset'):
            self.env.get_domain(RPG_DOMAIN).set_current_ruleset(
                self.env.docname, self.next_current_ruleset
            )

        return nodes

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=sig)

        if self.objtype == "ruleset":
            self.next_current_ruleset = sig

        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        domain = self.env.get_domain(RPG_DOMAIN)

        ruleset = self.options.get("ruleset", domain.current_ruleset(self.env.docname))
        new_object = domain.add_object(self.objtype, sig, ruleset=ruleset)
        signode["ids"].append(new_object.anchor)

    def get_object_type():
        return None


class RuleSetDirective(ForgeObjectDescription):
    def get_object_type():
        return "ruleset"


class CharacterDirective(ForgeObjectDescription):
    has_content = True

    def get_object_type():
        return "character"
