# -*- coding: utf-8 -*-

"""COSMOSTATMAP INFO

This module provides some basic information about the CosmoStatMap package.

:Author: Samuel Farrens <samuel.farrens@cea.fr>

"""

# Package Info
version_info = (0, 0, 0)
__version__ = '.'.join(str(c) for c in version_info)
__name__ = 'cosmostatmap'
__author__ = 'Samuel Farrens'
__email__ = 'samuel.farrens@cea.fr'
__about__ = ('The CosmoStatMap shows the diversity of the CosmoStat team.')
__setups__ = ['pytest-runner']
__installs__ = ['geoplot>=0.4.0',
                'pyyaml>=5.3.1']
__tests__ = ['pytest',
             'pytest-cov',
             'pytest-pep8']
