CosmoStat Map
=============

|python35| |python36| |python37| |python38|

.. |python35| image:: https://img.shields.io/badge/python-3.5-green.svg
  :target: https://www.python.org/

.. |python36| image:: https://img.shields.io/badge/python-3.6-green.svg
  :target: https://www.python.org/

.. |python37| image:: https://img.shields.io/badge/python-3.7-green.svg
  :target: https://www.python.org/

.. |python38| image:: https://img.shields.io/badge/python-3.8-green.svg
  :target: https://www.python.org/

  :Author: Samuel Farrens `(samuel.farrens@cea.fr) <samuel.farrens@cea.fr>`_

  :Version: 0.0.0

  :Release Date: 31/03/2020

  :Documentation: N/A

  :Repository: |link-to-repo|

  .. |link-to-repo| raw:: html

    <a href="https://github.com/CEA-COSMIC/ModOpt"
    target="_blank">https://github.com/CEA-COSMIC/ModOpt</a>

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
   python setup.py install


Example
-------

.. code-block:: python

   from cosmostatmap import CosmoStatMap
   CosmoStatMap('./data/countries.yml').plot()
