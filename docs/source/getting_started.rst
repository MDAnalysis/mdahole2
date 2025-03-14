Getting Started
===============

This page details how to get started with ``mdahole2``.
Note that ``mdahole2`` is currently only supported on Linux or macOS.

Documentation
~~~~~~~~~~~~~

Documentation is hosted on `GitHub Pages`_.

.. _`GitHub Pages`: https://www.mdanalysis.org/mdahole2/

Installation 
~~~~~~~~~~~~~~~~~~~~~~

``mdahole2`` can be installed in several ways:

From conda
----------

The recommended way to install ``mdahole2`` is through conda:

.. code:: bash

    conda install -c conda-forge mdahole2

If you already have ``hole2`` installed and want to use that version, you can install ``mdahole2`` without the ``hole2`` dependency:

.. code:: bash

    conda install -c conda-forge mdahole2-base

From pip
--------

You can also install ``mdahole2`` using pip:

.. code:: bash

    pip install mdahole2

Download and Build source code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``mdahole2`` source code is hosted on GitHub_ and can be downloaded with

.. code:: bash

	git clone git@github.com:MDAnalysis/mdahole2.git

with an SSH key, or with

.. code:: bash

	git clone https://github.com/MDAnalysis/mdahole2.git

.. _GitHub: https://github.com/MDAnalysis/mdahole2

To build ``mdahole2`` from source, we highly recommend using virtual environments, preferably with `Anaconda`_.

With conda:

.. code:: bash

    conda create --name mdahole2
    conda activate mdahole2
    conda env update --name mdahole2 --file devtools/conda-envs/test_env.yaml --file docs/requirements.yaml
    pip install -e .

With pip:

.. code:: bash

    pip install -e .

For development purposes, you can install additional test and documentation dependencies:

.. code:: bash

    pip install -e ".[test,doc]"

.. _Anaconda: https://docs.conda.io/en/latest/

Installing hole2
~~~~~~~~~~~~~~~~

``mdahole2`` requires the ``hole2`` executable to be installed.

This is most easily done using ``conda``, ``mamba``, or a similar
package manager. For example, to install ``hole2`` using ``mamba``:

.. code:: bash

	mamba install -c conda-forge hole2

Alternatively, ``hole2`` can be installed from the original HOLE_ website.

.. _HOLE: http://www.holeprogram.org