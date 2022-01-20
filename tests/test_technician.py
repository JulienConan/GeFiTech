from gefitech.models.technician import Technician

from datas.datas_test import base_technician

def test_create_tech():
    tech = Technician(base_technician)
    assert tech.firstname == "Sylvie"
    assert tech.surname == "Solo"
    return tech

def test_change_firstname():
    tech = Technician(base_technician)
    tech.modify_firstname("Paul")
    assert tech.firstname == "Paul"

def test_change_surname():
    tech = Technician(base_technician)
    tech.modify_surname("Personne")
    assert tech.surname == "Personne"

def test_serialize():
    tech = Technician(base_technician)
    tech_serialize = tech.serialize()
    assert tech_serialize == ["Sylvie", "Solo"]
