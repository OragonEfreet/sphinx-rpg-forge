from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx_rpg_forge.nodes import ruleset


class RuleSetDirective(Directive):
    required_arguments = 1

    def run(self):

        rs = ruleset()
        return [rs]

        paragraph_node = nodes.paragraph(text='Hello World!')
        return [paragraph_node]
