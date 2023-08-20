from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx_rpg_forge.nodes import RuleSetNode


class RuleSetDirective(Directive):
    required_arguments = 1

    option_spec = {
        'title': directives.unchanged_required,
    }

    def run(self):
        rs_id = self.arguments[0]
        rs_title = "Pouet"

        # Create and register the new rule set
        # self.env.rulesets[rs_id] = None

        # Create the node for doctree-resolve
        rs = RuleSetNode()
        rs.ruleset = rs_id
        return [rs]
