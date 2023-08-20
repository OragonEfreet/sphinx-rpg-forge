from docutils import nodes


class RuleSetNode(nodes.General, nodes.Element):
    pass


def process_ruleset_nodes(app, doctree, fromdocname):
    # This first version just replaces every RuleSetNode
    # with something else.
    for node in doctree.findall(RuleSetNode):
        node.replace_self([nodes.paragraph(text=node.ruleset)])


def setup(app):
    app.add_node(RuleSetNode)

    app.connect('doctree-resolved', process_ruleset_nodes)
