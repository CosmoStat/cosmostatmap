# -*- coding: utf-8 -*-

"""MAP ROUTINES

This module contains the class for making the CosmoStat Map.

:Author: Samuel Farrens <samuel.farrens@cea.fr>

"""

import yaml
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import geopandas as gpd
from descartes import PolygonPatch


class CosmoStatMap:
    '''CosmoStat Map

    This class produces a map of the origins of all current and former
    CosmoStat members.

    Parameters
    ----------
    file_name : str
        Full path to the input YAML file
    default_colour : str
        Default country colour (default is '#818181')
    current_colour : str
        Current members country colour (default is '#0092CF')
    former_colour : str
        Former members country colour (default is '#dbb578')
    water_colour : str
        Bodies of water colour (default is '#505050')
    border_colour : str
        Border between countries colour (default is '#7a7a7a')
    map_projection : int
        Map projection number (default is ``3395``)
    hide_antartica : bool
        Option to hide Antarctica from the map (default is ``True``)
    figsize : tuple
        Size of the output figure (default is ``(12, 8)``)

    '''

    def __init__(self, file_name, default_colour='#818181',
                 current_colour='#0092CF', former_colour='#dbb578',
                 water_colour='#505050', border_colour='#7a7a7a',
                 map_projection=3395, hide_antartica=True, figsize=(12, 8)):

        self.file_name = file_name

        # Set map properties
        self._default_colour = default_colour
        self._current_colour = current_colour
        self._former_colour = former_colour
        self._water_colour = water_colour
        self._border_colour = border_colour
        self._map_projection = map_projection
        self._hide_antartica = hide_antartica
        self._figsize = figsize

        # Read world map from Geopandas
        self.world = gpd.read_file(gpd.datasets.get_path(
                                   'naturalearth_lowres'))

        # Read the input file
        self._read_yaml()

    def _read_yaml(self):
        '''Read YAML

        Read the input yaml file to extract the countries dictionary.

        '''

        with open(self.file_name) as f:

            self.countries_dict = yaml.load(f, Loader=yaml.FullLoader)

    def _highlight_country(self, country, colour):
        '''Highlight Country

        Highlight the country with the specified colour.

        Parameters
        ----------
        country : str
            Country names
        colour : str
            Colour name or hex code

        '''

        name = (self.world[self.world.name ==
                country].__geo_interface__['features'])
        namig0 = {'type': name[0]['geometry']['type'],
                  'coordinates': name[0]['geometry']['coordinates']}
        self._axis.add_patch(PolygonPatch(namig0, fc=colour,
                             ec=self._border_colour, alpha=0.85, zorder=2))

    def _add_country_from_list(self, country_list, colour):
        '''Add Country from List

        Add countries to the world map from the provided list. Highlight the
        countries with the specified colour.

        Parameters
        ----------
        country_list : list
            List of country names
        colour : str
            Colour name or hex code

        '''

        for country in country_list:
            self._highlight_country(country, colour)

    def _make_plot(self, **kwargs):
        '''Make Plot

        Plot CosmoStat map.

        '''

        # Switch to Mercator projection
        self.world = self.world.to_crs(epsg=self._map_projection)

        # Remove Antarctica
        if self._hide_antartica:
            self.world = self.world[(self.world.name != "Antarctica")]

        # Create a shared axis
        _, self._axis = plt.subplots(figsize=self._figsize)

        # World map
        self.world.plot(ax=self._axis, color=self._default_colour,
                        edgecolor=self._border_colour, **kwargs)

        # Highlight countries in map
        self._add_country_from_list(self.countries_dict['current'],
                                    self._current_colour)
        self._add_country_from_list(self.countries_dict['former'],
                                    self._former_colour)

        # Set water colour
        self._axis.set_facecolor(self._water_colour)

        # Set axis labels
        plt.ylabel('Latitude')
        plt.xlabel('Longitude')

        custom_lines = [Line2D([0], [0], color=self._current_colour, lw=5),
                        Line2D([0], [0], color=self._former_colour, lw=5)]

        self._axis.legend(custom_lines, ['Current Members', 'Former Members'])

    def show(self, **kwargs):
        '''Plot

        Show CosmoStat map.

        '''

        self._make_plot(**kwargs)

        # Show Map
        plt.show()

    def save(self, file_name='cosmostat_map.png', **kwargs):
        '''Save

        Save CosmoStat map.

        '''

        self._make_plot(**kwargs)

        # Show Map
        plt.savefig(file_name, transparent=True)
