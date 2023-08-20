############
Contributing
############

Install the development prerequisites
=====================================

Run ``pip install -r requirements.txt`` to install all the necessary Python packages for developping the extension.
This covers all use cases presented below.
You can still individually install each package instead with ``pip install package-name``.
Each section below gives the list of the minimal package it needs.

In any case, it is advised to use a `Python virtual environment <https://docs.python.org/3/library/venv.html#creating-virtual-environments>`__ in order to avoid bloating your system:

.. code:: console

   python -m venv .venv
   source .venv/bin/activate.sh

This example is for bash shells `go here <https://docs.python.org/3/library/venv.html#how-venvs-work>`__ for other shells.

Testing with TOX
================

.. sidebar:: 

   Required package: ``tox``.

Build the documentation
-----------------------

Use to following comment to build the documentation.

.. code::console

   tox -e html

The documentation will be generated in *.tox/html/tmp/html*.

Serve the documentation
-----------------------

With:

.. code:: console

   tox -e serve -- 8080

The documentation is built and served on ``http://127.0.0.1:8080``.
Any change made to the _docs/_ folder will automatically regenerate the documentation and reload the browser.

You can select the port you want, or use automatically any available port with ``tox -e serve``.

Run static analysis
-------------------

The ``tox`` command with no argument will run a type checking analysing and linting or your extension source folder.
To run the command individually, use ``tox -e typecheck`` and ``tox -e lint`` respectively.

Building the documentation without TOX
======================================

.. sidebar::

   Required packages: *docs/requirements.txt*.

You can build the documentation in a more Sphinx-traditional way.

- Change to the *docs/* folder
- Install the required Python package using ``pip install -r ./requirements.txt``
- Install the extension using ``pip install -e ..``
- Run ``make html``
- The documentation is available at */docs/build/html/*

.. note:: 

   The ``-e`` option makes your package editable, which means that Sphinx will directly use your source code instead of an isolated package.
   With this, your can make changes to your source code and run ``make html`` without the need to reinstall your package again.

Building the extension's package
================================

.. sidebar::

   Required package: ``build``

Run ``pyproject-build`` from the root of the repository.
The package is generated in the *dist/* folder.

Making changes to the extension
===============================

Versioning
----------

The version of the extension is set in the ``__version__`` variable at *src/sphinx_rpg_forge/__init__.py*.
This is the only place the version is and should be set in order to ensure a consistent version in the package.

Documentation
-------------

The *docs/* folder contains a Sphinx documentation that is automatically built against sphinx_rpg_forge.




