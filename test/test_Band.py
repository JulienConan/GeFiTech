from patch_test import patch_test
from band import Band
from technician import Technician

base_tech = {'firstname' : "John", 'surname' : "Doe", 'role' : "tech"}

base_band = {'name' : 'SuperBand',
             'rider_date' : {'year' : 2000, 'month' : 1, 'day' : 1}, 
             'foh_technician' : base_tech,
             'monitor_technician' : base_tech,
             'patch' : patch_test }


test_band = Band(base_band)
"""print(test_band)
print("Taille du patch : " + str(len(test_band.patch)))
print(test_band.count_items('reference'))
print(test_band.count_items('stand'))"""