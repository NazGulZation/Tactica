from Model.UnitType import UnitType


def add_unit_type(repo, name, hp, is_ranged, damage):
    """
    Create and add a new unit type to the repository.
    
    Args:
        repo (Repo): The repository instance where unit types are stored.
        name (str): The name of the unit type.
        hp (int): The health points of the unit type.
        is_ranged (bool): Whether the unit type is ranged.
        damage (int): The damage value for the unit type.
        
    Returns:
        UnitType: The newly created unit type object.
    """
    unit_type = UnitType(repo, name, hp, is_ranged, damage)
    return unit_type