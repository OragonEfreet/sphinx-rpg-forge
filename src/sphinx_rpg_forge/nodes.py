from docutils import nodes


class ruleset(nodes.Admonition, nodes.Element):
    pass


def visit_ruleset_node(self, node):
    print('visit_ruleset_node')
    self.visit_admonition(node)


def depart_ruleset_node(self, node):
    print('depart_ruleset_node')
    self.depart_admonition(node)


def setup(app):
    app.add_node(ruleset, html=(visit_ruleset_node, depart_ruleset_node))
