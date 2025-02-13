from Model.Repo import Repo
from Model.Game import Game
from Model.Player import Player
from Model.Map import Map
from Model.UnitType import UnitType
from Model.Unit import Unit

if __name__ == "__main__":
    repo = Repo()
    
    # Create a new game object
    game = Game(repo, "Battle of Python")
    # Create a player associated with the game
    player = Player(repo, game_id=game.id, name="Alice")
    # Create a map for the game
    game_map = Map(repo, game_id=game.id, x_size=10, y_size=10)
    # Create a unit type
    infantry = UnitType(repo, name="Infantry", hp=100, is_ranged=False, damage=10)
    # Create a unit belonging to the player on the map
    unit = Unit(repo, unit_type_id=infantry.id, map_id=game_map.id, player_id=player.id, x=5, y=5)
    
    # Retrieve and print all objects in the repo
    for obj in repo.get():
        print(obj)