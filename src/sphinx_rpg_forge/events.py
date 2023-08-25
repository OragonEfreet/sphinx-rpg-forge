from sphinx_rpg_forge.constants import RPG_DOMAIN

def env_purge_doc(app, env, docname):
    # Remove the current 
    domain = env.get_domain(RPG_DOMAIN)
    domain.set_current_ruleset(docname, None)

def setup(app):
    app.connect("env-purge-doc", env_purge_doc)

