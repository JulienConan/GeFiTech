# coding: utf-8
"""Module for Technician's Class"""


class Technician:
    """ Create a Technician's Object"""

    def __init__(self, tech):
        self.firstname = tech['firstname']
        self.surname = tech['surname']
        self.role = tech['role']

    def __repr__(self):
        return self.firstname + " " + self.surname

    def __str__(self):
        return repr(self)

    def modify_firstname(self, new_firstname):
        self.firstname = new_firstname

    def modify_surname(self, new_surname):
        self.surname = new_surname

    def modify_role(self, new_role):
        self.role = new_role



