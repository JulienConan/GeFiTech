# coding: utf-8
"""Module for Technician's Class"""

import datetime

from technician import Technician

class Band:
    """ Create a Band's Object"""

    def __init__(self, band_infos):
        self.name = band_infos['name']
        self.rider_date = datetime.datetime(band_infos['rider_date']['year'], 
                                            band_infos['rider_date']['month'], 
                                            band_infos['rider_date']['day'])
        self.foh_technician = Technician(band_infos['foh_technician'])
        self.monitor_technician = Technician(band_infos['monitor_technician'])
        self.patch = band_infos['patch']

    def __repr__(self):
        return 'Groupe : ' + self.name + " - " + self.rider_date.strftime("%d %B %Y")

    def __str__(self):
        return repr(self)

    def modify_name(self, new_name):
        self.name = new_name

    def modify_rider_date(self, new__rider_date):
        self.rider_date = new_rider_date

    def modify_foh_technician(self, new_foh_technician):
        self.foh_technician = new_foh_technician

    def modify_monitor_technician(self, new_monitor_technician):
        self.monitor_technician = new_monitor_technician

    def count_items(self, item):
        count_list={}
        for source in self.patch:
            if (source[item] in count_list):
                count_list[source[item]] += 1
            else:
                count_list[source[item]] = 1
        return count_list

