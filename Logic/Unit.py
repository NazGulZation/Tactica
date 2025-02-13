from Model.Unit import Unit
from Model.UnitType import UnitType


def add_unit(repo, unit_type_id, map_id, player_id, x, y):
    """
    Create and add a new unit to the repository using provided ids.
    
    The unit's health points (hp) are retrieved from the corresponding unit type's default hp.
    
    Args:
        repo (Repo): The repository instance where units and unit types are stored.
        unit_type_id (str): The id of the unit type for the new unit.
        map_id (str): The id of the map on which the unit will be placed.
        player_id (str): The id of the player who owns the unit.
        x (int): The x-coordinate position of the unit on the map.
        y (int): The y-coordinate position of the unit on the map.
    
    Returns:
        Unit: The newly created unit object.
    
    Raises:
        ValueError: If the unit type with the given id is not found in the repository.
    """
    # Retrieve the unit type to obtain its default hp
    unit_types = repo.get(UnitType, lambda ut: ut.id == unit_type_id)
    if not unit_types:
        raise ValueError(f"UnitType with id {unit_type_id} not found in the repository.")
    unit_type = unit_types[0]
    
    # Create a new unit using the retrieved hp from unit_type
    unit = Unit(repo, unit_type_id, map_id, player_id, x, y, unit_type.hp)
    return unit
