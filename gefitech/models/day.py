# coding: utf-8
"""Module for Day's Class"""
from gefitech.models.band import Band

class Day:
    """ Create a Day's Object"""

    def __init__(self, day):
        """Round object initialisation"""
        self.date = [day['date']['year'], day['date']['month'], day['date']['day']]
        self.band_list = [Band(band) for band in day['band_list']]

    def __repr__(self):
        return self.date

    def __str__(self):
        return repr(self)

    def add_band(self, band):
        self.band_list.append(Band(band))

    def remove_Band(self, band):
        pass
