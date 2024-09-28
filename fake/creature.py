from model.creature import Creature

_creatures = [
    Creature(name = "Mr. Rado",
             aka = "Szczur politechniczny",
             country = "US",
             area = "*",
             description = "Coś się wymyśli :)!!!"),
    Creature(name = "Herr Tusk",
             aka = "fur deutschland",
             country = "DE",
             area = "Berlin",
             description = "Zdrajca polski uważać na niego"),
]

def get_all() -> list[Creature]:
    """Zwróć wszystkie stworzenia"""
    return _creatures

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
        return None

def create(creature: Creature) -> Creature:
    """Dodaj nowego odkrywcę"""
    return creature

def modify(creature: Creature) -> Creature:
    """Częściowo zmodyfikuj odkrywcę"""
    return creature

def replace(creature: Creature) -> Creature:
    """Zastąp całkowicie odkrywcę"""
    return creature

def delete(name: str):
    """Usuń odkrywce, zwróć None, jeśli istniał."""
    return None