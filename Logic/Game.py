from Model.Game import Game
from Model.Map import Map
from Model.Player import Player

def start_game(repo, game_name, map_x_size, map_y_size, player_names):
    """
    Create and start a new game, initializing the game, its map, and its players.
    
    Args:
        repo (Repo): The repository instance where game objects are stored.
        game_name (str): The name for the new game.
        map_x_size (int): Width of the game map.
        map_y_size (int): Height of the game map.
        player_names (list): List of player names. The first player in the list is assigned as the current player.
    
    Returns:
        Game: The newly created game object.
    """
    # Create a new game instance
    game = Game(repo, game_name)
    
    # Create a new map for the game and assign it to the current map
    game_map = Map(repo, game.id, map_x_size, map_y_size)
    game.current_map = game_map
    
    # Create players for the game from the provided list of names
    players = [Player(repo, game.id, name) for name in player_names]
    game.current_player = players[0]
    
    return game

