from Model.Map import Map
from Model.Unit import Unit


def draw_map(map_id, repo):
    """
    Draws the map as an ASCII grid with each cell separated by horizontal and vertical lines.
    The grid uses 1-indexed coordinates for placement. Empty cells are denoted by '.', and cells with a unit are denoted by 'X'.

    Args:
        map_id (str): The id of the map to be drawn.
        repo (Repo): The repository instance that contains Map and Unit objects.
    """
    # Retrieve the map object using its id
    maps = repo.get(Map, lambda m: m.id == map_id)
    if not maps:
        print("Map not found in the repository.")
        return
    map_obj = maps[0]

    # Retrieve all units on this map using the map_id
    units_on_map = repo.get(Unit, lambda unit: unit.map_id == map_id)

    # Build a 2D grid representing the map with cell symbols.
    # Now using 1-indexed coordinates: rows from 1 to y_size and columns from 1 to x_size.
    grid = []
    for y in range(1, map_obj.y_size + 1):
        row = []
        for x in range(1, map_obj.x_size + 1):
            # Mark cell with 'X' if a unit is found at (x, y), otherwise mark with '.'
            if any(unit.x == x and unit.y == y for unit in units_on_map):
                row.append("X")
            else:
                row.append(".")
        grid.append(row)

    # Define cell width for proper spacing (each cell is rendered as " X " or " . ")
    cell_width = 3
    # Generate horizontal separator line for one row of cells
    horizontal_line = "+" + ("-" * cell_width + "+") * map_obj.x_size

    # Draw the grid with horizontal and vertical separators
    for row in grid:
        print(horizontal_line)
        # Construct the row with vertical borders between cells
        row_str = ""
        for cell in row:
            row_str += f"| {cell} "
        row_str += "|"
        print(row_str)
    print(horizontal_line)