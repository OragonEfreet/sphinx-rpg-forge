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

    # def run(self) -> list[Node]:
    #     super().run()
    
    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=sig)

        # Set the current ruleset
        if 'ruleset' in self.options:
            domain = self.env.get_domain(RPG_DOMAIN)
            old = domain.current_ruleset(self.env.docname)
            domain.set_current_ruleset(self.env.docname, self.options['ruleset'])
            new = domain.current_ruleset(self.env.docname)

            print("=========")
            print(f"While parsing '{sig}'")
            print(f"Changed ruleset from '{old}' to '{new}'")
            print("=========")

        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        domain = self.env.get_domain(RPG_DOMAIN)
        new_object = domain.add_object(self.objtype, sig, ruleset=self.options.get("ruleset", None))
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
