__version__ = "0.0.1"


def setup(app):
    from sphinx_rpg_forge.domains import ForgeDomain
    from sphinx_rpg_forge.nodes import setup as setup_nodes

    app.add_domain(ForgeDomain)
    setup_nodes(app)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
