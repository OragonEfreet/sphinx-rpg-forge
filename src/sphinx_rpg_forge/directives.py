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
    final_argument_whitespace = False
    required_arguments = 1
    option_spec = {
        'title': directives.unchanged_required,
        'noindex': directives.flag,
    }

    def handle_signature(self, sig, signode):
        self.dispname = self.options.get('title', sig)
        signode += addnodes.desc_name(text=self.dispname)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode['ids'].append(self.env.get_domain(
            RPG_DOMAIN).add_ruleset(sig, self.dispname))
