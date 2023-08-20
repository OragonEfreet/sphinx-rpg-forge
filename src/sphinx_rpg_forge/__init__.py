##############################################################################
# Sphinx RPG Forge
# Package/Module: sphinx-rpg-forge/sphinx_rpg_forge
# Created by: kevin.dorange@protonmail.com
# A Sphinx Docs extension for generating RPG scenarios
##############################################################################
# This file has been created automatically from the "Hello World" extension
# example available at
# - https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html
# Feel free to start from here and create your own extension.
#
##############################################################################
# To ensure a seamless build of this package, PLEASE DON'T IMPORT ANY
# NON-BUILTIN PACKAGE AT __init__.py LEVEL.
# If your setup function needs to import something, do it from within the
# function.
# This restriction only applies to this file and no other module files you
# may create for your extension.
##############################################################################

# This is the single place the version is set for the entire package.
__version__ = "0.0.1"


def setup(app):
    from sphinx_rpg_forge.directives import HelloWorld

    app.add_directive("helloworld", HelloWorld)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
