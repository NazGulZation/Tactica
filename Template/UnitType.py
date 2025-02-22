from Logic.UnitType import add_unit_type

def add_infantry(repo, name="Infantry", hp=100, is_ranged=False, damage=10):
    return add_unit_type(repo, name, hp, is_ranged, damage)

def add_swordman(repo, name="Swordman", hp=120, is_ranged=False, damage=12):
    return add_unit_type(repo, name, hp, is_ranged, damage)

def add_scout(repo, name="Scout", hp=80, is_ranged=False, damage=8):
    return add_unit_type(repo, name, hp, is_ranged, damage)

def add_footman(repo, name="Footman", hp=100, is_ranged=False, damage=10):
    return add_unit_type(repo, name, hp, is_ranged, damage)