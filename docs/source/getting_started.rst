Getting Started
===============

This page details how to get started with ``mdahole2``.
Note that ``mdahole2`` is currently only supported on Linux or macOS.

Documentation
~~~~~~~~~~~~~

Documentation is hosted on `GitHub Pages`_.

.. _`GitHub Pages`: https://www.mdanalysis.org/mdahole2/

Download source code
~~~~~~~~~~~~~~~~~~~~

The ``mdahole2`` source code is hosted on GitHub_ and can be downloaded with

.. code:: bash

	git clone git@github.com:MDAnalysis/mdahole2.git

with an SSH key, or with

.. code:: bash

	git clone https://github.com/MDAnalysis/mdahole2.git

.. _GitHub: https://github.com/MDAnalysis/mdahole2

Build and installation
~~~~~~~~~~~~~~~~~~~~~~

``mdahole2`` is currently only installable from source (although hosting on conda-forge is planned).
As such ``conda-build`` is required. To download this utility, invoke:

.. code:: bash

	conda install conda-build

From the repository root directory, run

.. code:: bash

	conda build . && conda install --use-local mdahole2

to build the package and install the local build.

Installing hole2
~~~~~~~~~~~~~~~~

``mdahole2`` requires the ``hole2`` executable to be installed.

This is most easily done using ``conda``, ``mamba``, or a similar
package manager. For example, to install ``hole2`` using ``mamba``:

.. code:: bash

	mamba install -c conda-forge hole2

Alternatively, ``hole2`` can be installed from the original HOLE_ website.

.. _HOLE: http://www.holeprogram.org