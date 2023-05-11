Getting Started
===============

This page details how to get started with `mdahole2`.

Documentation
~~~~~~~~~~~~~

Documentation is hosted on `Read the Docs`_.

.. _`Read the Docs`: https://mdahole2.readthedocs.io/en/latest/

Download source code
~~~~~~~~~~~~~~~~~~~~

The `mdahole2` source code is hosted on GitHub_ and can be downloaded with

.. code:: bash

	git clone git@github.com:MDAnalysis/hole2-mdakit.git

with an SSH key, or with

.. code:: bash

	git clone https://github.com/MDAnalysis/hole2-mdakit.git

.. _GitHub: https://github.com/MDAnalysis/hole2-mdakit

Build and installation
~~~~~~~~~~~~~~~~~~~~~~

`mdahole2` is currently only installable from source (although hosting on conda-forge is planned).
As such `conda-build` is required. To download this utility, invoke:

.. code:: bash

	conda install conda-build

From the repository root directory, run

.. code:: bash

	conda build . && conda install --use-local mdahole2

to build the package and install the local build.
