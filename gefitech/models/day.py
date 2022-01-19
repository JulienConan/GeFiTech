# coding: utf-8
"""Module for Day's Class"""

class Day:
    """ Create a Day's Object"""

    def __init__(self, date=None, band_list="null"):
        """Round object initialisation"""
        self.date = date
        self.band_list = band_list

    def __repr__(self):
        return self.date

    def __str__(self):
        return repr(self)
