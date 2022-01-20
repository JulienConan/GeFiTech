# coding: utf-8
"""Module for Technician's Class"""


class Technician:
    """ Create a Technician's Object"""

    def __init__(self, tech=[]):
        self.firstname = tech[0]
        self.surname = tech[1]

    def __repr__(self):
        return self.firstname + " " + self.surname

    def __str__(self):
        return repr(self)

    def modify_firstname(self, new_firstname):
        self.firstname = new_firstname

    def modify_surname(self, new_surname):
        self.surname = new_surname

    def serialize(self):
        tech_serialize = [self.firstname, self.surname]
        return tech_serialize

    def __eq__(self, other):
        if isinstance(other, Technician):
            return (self.firstname == other.firstname and self.surname == other.surname)
        return False
        """""""
