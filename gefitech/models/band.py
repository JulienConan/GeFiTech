"""Summary
"""
# coding: utf-8
"""Module for Technician's Class"""

import datetime


class Band:
    """Create a Band's Object
    
    Attributes:
        foh_technician (TYPE): Description
        monitor_technician (TYPE): Description
        name (TYPE): Description
        patch (TYPE): Description
        rider_date (TYPE): Description
    """

    def __init__(self, band_infos):
        """Summary
        
        Args:
            band_infos (TYPE): Description
        """
        self.name = band_infos['name']
        self.rider_date = [band_infos['rider_date']['year'],
                            band_infos['rider_date']['month'],
                            band_infos['rider_date']['day']]
        self.foh_technician = band_infos['foh_technician']
        self.monitor_technician = band_infos['monitor_technician']
        self.patch = band_infos['patch']

    def __repr__(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return 'Groupe : ' + self.name + " - " + self.rider_date.strftime("%d %B %Y")

    def __str__(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return repr(self)

    def modify_name(self, new_name):
        """Summary
        
        Args:
            new_name (TYPE): Description
        """
        self.name = new_name

    def modify_rider_date(self, new_rider_date):
        """Summary
        
        Args:
            new_rider_date (TYPE): Description
        """
        self.rider_date = new_rider_date

    def modify_technician(self, role, new_technician):
        """Summary
        
        Args:
            role (TYPE): Description
            new_technician (TYPE): Description
        """
        if role == "foh":
            self.foh_technician = new_technician
        elif role == "monitor":
            self.monitor_technician = new_technician
        else:
            pass

    def count_items(self, item):
        """Summary
        
        Args:
            item (TYPE): Description
        
        Returns:
            TYPE: Description
        """
        count_list={}
        for source in self.patch:
            if (source[item] in count_list):
                count_list[source[item]] += 1
            else:
                count_list[source[item]] = 1
        return count_list

    def count_all(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        full_item = {}
        full_item["references"] = self.count_items('reference')
        full_item['stand'] = self.count_items('stand')
        return full_item