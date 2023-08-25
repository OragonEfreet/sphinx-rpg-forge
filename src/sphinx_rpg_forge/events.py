from sphinx_rpg_forge.constants import RPG_DOMAIN


def env_purge_doc(app, env, docname):
    # Remove the current domain for this docname
    domain = env.get_domain(RPG_DOMAIN)
    domain.set_current_ruleset(docname, None)

def  build_finished(app, exception):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(app.env.get_domain(RPG_DOMAIN).data)


def setup(app):
    app.connect("env-purge-doc", env_purge_doc)
    app.connect("build-finished", build_finished)
    
