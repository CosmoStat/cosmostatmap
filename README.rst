CosmoStat Map
=============

|actions|

.. |actions| image:: https://github.com/CosmoStat/cosmostatmap/workflows/CI/badge.svg?branch=master
  :target: https://github.com/CosmoStat/cosmostatmap/actions

:Author: Samuel Farrens `(samuel.farrens@cea.fr) <samuel.farrens@cea.fr>`_

:Version: 0.0.0

:Release Date: 31/03/2020

.. |link-to-docs| raw:: html

  <a href="https://sfarrens.github.io/cosmostatmap"
  target="_blank">https://sfarrens.github.io/cosmostatmap</a>

.. |link-to-repo| raw:: html

  <a href="https://github.com/sfarrens/cosmostatmap"
  target="_blank">https://github.com/sfarrens/cosmostatmap</a>

Requirements
------------

- `GeoPandas <https://geopandas.org/>`_
- `geoplot <https://residentmario.github.io/geoplot/index.html>`_
- `Jupyter <https://jupyter.org/>`_
- `Matplotlib <https://matplotlib.org/>`_
- `PyYAML <https://pyyaml.org/>`_

Installation
------------

.. code-block:: bash

   conda env create -f environment.yml
   conda activate cosmostatmap
   python -m pip install .


Example
-------

.. code-block:: python

   from cosmostatmap import CosmoStatMap
   CosmoStatMap('./data/countries.yml').show()
