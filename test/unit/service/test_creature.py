from pydoc import describe

from model.creature import Creature
from service import creature as code

sample = Creature(name="Psikuta",
                  country="PL",
                  area = "Cała Polska",
                  description = "Ważne!!! bez S",
                  aka = "Psikutas")

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exist():
    resp = code.get_one("Psikuta")
    assert resp == sample

def test_get_missing():
    resp = code.get_one("Arnold Boczek")
    assert resp is None