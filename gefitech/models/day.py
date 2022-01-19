# coding: utf-8
"""Module for Day's Class"""

from gefitech.models.band import band_list

class Day:
    """ Create a Day's Object"""

    def __init__(self, date, band_list):
        """Round object initialisation"""
        self.date = [{"year" : ]date['year'],
        self.band_list = [Band(band) for band in band_list]

    def __repr__(self):
        return self.date

    def __str__(self):
        return repr(self)


