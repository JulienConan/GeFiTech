"""Summary
"""
# coding: utf-8
"""Module for Technician's Class"""

import datetime


class Band:
    """Create a Band's Object"""

    def __init__(self, band_infos):

        self.name = band_infos['name']
        self.rider_date = [band_infos['rider_date']['year'],
                            band_infos['rider_date']['month'],
                            band_infos['rider_date']['day']]
        self.foh_technician = band_infos['foh_technician']
        self.monitor_technician = band_infos['monitor_technician']
        self.patch = band_infos['patch']

    def __repr__(self):
        return 'Groupe : ' + self.name + " - " + self.rider_date.strftime("%d %B %Y")

    def __str__(self):
        return repr(self)

    def count_items(self, item):
        count_list={}
        for source in self.patch:
            if (source[item] in count_list):
                count_list[source[item]] += 1
            else:
                count_list[source[item]] = 1
        return count_list

    def count_all(self):
        full_item = {}
        full_item["references"] = self.count_items('reference')
        full_item['stand'] = self.count_items('stand')
        return full_item
