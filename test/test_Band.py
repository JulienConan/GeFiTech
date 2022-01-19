import json
import datetime

from gefitech.models.band import Band
from gefitech.models.technician import Technician

from datas.datas_test import base_band

def test_create_band():
    band = Band(base_band)
    assert band.name == "Groupe1"
    assert band.rider_date == [2000, 1, 1]
    assert band.foh_technician == ["Julien", "CONAN"]
    assert band.monitor_technician == ["Piotr", "Skotnicki"]
    assert band.patch == base_band["patch"]

def test_count_items():
    band = Band(base_band)
    count_items = band.count_items('reference')
    assert count_items == {"SM91" : 1, "SM57" : 1,  "BETA52" : 1}

def test_modify_name():
    band = Band(base_band)
    band.modify_name("groupe2")
    assert band.name == "groupe2"

def test_modify_rider_date():
    band = Band(base_band)
    band.modify_rider_date([2000,2,2])
    assert band.rider_date == [2000,2,2]

def test_modify_technician():
    band = Band(base_band)
    band.modify_technician("foh",["Julie", "ROUSSEAU"])
    assert band.foh_technician == ["Julie", "ROUSSEAU"]
