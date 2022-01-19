# coding: utf-8
"""Module for Event's Class"""

from day import Day

class Event:
    """ Create a Event's Object"""

    def __init__(self, name, date, day_list=[]):
        """Round object initialisation"""
        self.name = name
        self.date = date
        self.day_list =[Day(day) for day in day_list]
        self.local_foh_technician = band_infos['foh_technician']
        self.local_monitor_technician = band_infos['monitor_technician']


    def __repr__(self):
        return self.name + " - " + self.date

    def __str__(self):
        return repr(self)

    def modify_name(self, new_name):
        self.name = new_name

    def modify_date(self, new_date):
        self.date = new_date

    def add_new_day(self):
        self.day_list.append(Day())

    def remove_day(self,date):
        return

    def serialyse(self):
