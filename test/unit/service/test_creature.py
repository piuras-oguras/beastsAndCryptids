from pydoc import describe

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from model.creature import Creature
from service import creature as code

sample = Creature(name="Psikuta",
                  country="PL",
                  area = "Cała Polska",
                  description = "Ważne!!! bez S",
                  aka = "Psikutas")

sample2 = Creature(name = "Herr Tusk",
             aka = "fur deutschland",
             country = "DE",
             area = "Berlin",
             description = "Zdrajca polski uważać na niego")
def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exist():
    resp = code.get_one("Herr Tusk")
    assert resp == sample2

def test_get_missing():
    resp = code.get_one("Arnold Boczek")
    assert resp is None