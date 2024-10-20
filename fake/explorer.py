from model.explorer import Explorer

_explorers = [
    Explorer(name = "Menel pływak",
             country = "PL",
             description = "Poszukiwacz w skarbu w jeziorze"),
    Explorer(name = "Adolf Kitler",
             country = "DE",
             description = "Poszukiwacz zaginionej saszetki z kocim jedzeniem MIAU")
]

def get_all() -> list[Explorer]:
    """Zwróć wszystkich odkrywców"""
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    """Dodaj nowego odkrywcę"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Częściowo zmodyfikuj odkrywcę"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Zastąp całkowicie odkrywcę"""
    return explorer

def delete(name: str) -> bool:
    """Usuń odkrywce, zwróć None, jeśli istniał."""
    return None