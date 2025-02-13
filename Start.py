from Logic.Game import start_game
from Logic.Map import draw_map
from Logic.Player import get_players
from Logic.Unit import add_unit
from Logic.UnitType import add_unit_type
from Repo import Repo

if __name__ == '__main__':
    # Initialize the repository
    repo = Repo()

    # Start a new game with a map of size 10x5 and two players: Alice and Bob.
    game = start_game(repo, "Test Game", 10, 5, ["Alice", "Bob"])
    
    # Add a unit type, e.g., "Infantry"
    infantry_type = add_unit_type(repo, "Infantry", hp=100, is_ranged=False, damage=10)
    
    # Add a unit for the current player (Alice) at position (2, 2)
    alice_unit = add_unit(repo, infantry_type.id, game.current_map.id, game.current_player.id, x=2, y=2)
    
    # Retrieve Bob using the new get_players function.
    bob_list = get_players(repo, game.id, lambda player: player.name == "Bob")
    if bob_list:
        bob = bob_list[0]
        # Add a unit for Bob at position (5, 3)
        bob_unit = add_unit(repo, infantry_type.id, game.current_map.id, bob.id, x=5, y=3)
    
    # Draw the map; units are denoted by 'X' and empty spaces by '.'
    draw_map(game.current_map.id, repo)