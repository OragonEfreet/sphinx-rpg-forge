############
Installation
############

Install the ``sphinx-rpg-forge`` package (or add it to your ``requirements.txt`` file).
An additional repository URL must be provided to access TS3D packages:

.. code:: console

    $ pip install sphinx-rpg-forge

In your Sphinx project's ``conf.py`` file, add ``sphinx_rpg_forge`` to the list of enabled extensions.

.. code:: python

    extensions = [
        ...
        'sphinx_rpg_forge',
    ]

You're all set for :doc:`configuring`!





