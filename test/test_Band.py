import json
import datetime

from gefitech.models.band import Band

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
    count_sources = band.count_items('reference')
    count_stand = band.count_items('stand')
    assert count_sources == {"SM91" : 1, "SM57" : 1,  "BETA52" : 1}
    assert count_stand == {"GP" : 1, "PP" : 2}

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
    band.modify_technician("monitor",["Julien", "ROUSSEAU"])
    assert band.foh_technician == ["Julie", "ROUSSEAU"]
    assert band.monitor_technician == ["Julien", "ROUSSEAU"]

def test_count_all():
    band = Band(base_band)
    assert band.count_all() == {"references" : {"SM91" : 1, "SM57" : 1,  "BETA52" : 1},
                                "stand" : {"GP" : 1, "PP" : 2}}
