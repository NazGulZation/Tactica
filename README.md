# Tactica - Python Tactical Game Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Tactica** is a simple, extensible Python-based engine for creating turn-based tactical games. It provides a clear and modular foundation for game logic, map management, player and unit handling, and a basic in-memory repository. Designed for learning and prototyping, Tactica allows you to quickly set up and experiment with tactical game mechanics. This project is in its early stages and aims to grow into a more comprehensive framework for tactical game development.

## Key Features

*   **Turn-Based Game Management:**  Provides core components to create and manage turn-based game instances, define game names, and control game flow.
*   **Flexible Map System:** Define maps of varying sizes and represent game worlds as grid-based environments, ready for unit deployment and tactical maneuvering.
*   **Player and Faction Management:**  Easily add and manage multiple players within a game, each with unique names and controlled units.  Future versions can be extended to include factions or teams.
*   **Unit Types and Detailed Units:** Define diverse unit types with customizable attributes like health, damage type (ranged/melee), and base damage. Create individual units based on these types, placing them on the game map and assigning ownership to players.
*   **Lightweight In-Memory Repository:** Employs a straightforward in-memory repository for managing game objects (Games, Maps, Players, Units, Unit Types). This simplifies setup and is perfect for rapid prototyping, tutorials, and small-scale projects, eliminating the need for external databases.
*   **Basic Text-Based Map Visualization:** Offers a simple, text-based representation of the game map in the console, clearly displaying unit positions for immediate visual feedback and debugging.
*   **Extensible and Modular Design:** The engine is built with a modular design, making it easy to extend and customize different aspects of the game logic or add new features as needed.

## Getting Started

### Prerequisites

*   **Python 3.8 or higher:**  Tactica is written in Python and requires Python 3.8 or a later version to run. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

No installation is required! Tactica is designed to be run directly from the project directory. Simply clone or download the repository to your local machine.

```bash
git clone [repository-url] # Replace [repository-url] with the actual repository URL
cd Tactica
```

### Running the Example Game

To see Tactica in action, run the `Start.py` file directly. This script initializes a sample game, defines a unit type ("Infantry"), adds units for two players, and then visualizes the game map in your console.

```bash
python Start.py
```

You should see a text-based output in your console representing the game map grid, with 'X' symbols indicating unit positions and '.' for empty spaces.

## Usage

The `Start.py` file provides a fundamental example of how to interact with the Tactica engine. Below are more details and expanded examples to help you get started:

1.  **Initialize the Repository:**  Begin by creating an instance of the `Repo` class. This in-memory repository will store all game objects during runtime.
    ```python
    repo = Repo()
    ```

2.  **Start a New Game:** Use the `start_game` function to instantiate a new game. Define the game name, map dimensions, and the names of the players participating.
    ```python
    from Logic.Game import start_game
    game = start_game(repo, "Epic Battle", 20, 10, ["Commander Red", "General Blue"])
    ```

3.  **Define Unit Types:** Create various unit types using `add_unit_type`. Customize attributes like `hp`, `is_ranged`, and `damage` to define unique unit roles.
    ```python
    from Logic.UnitType import add_unit_type
    archer_type = add_unit_type(repo, "Archer", hp=70, is_ranged=True, damage=15)
    knight_type = add_unit_type(repo, "Knight", hp=150, is_ranged=False, damage=20)
    ```
    You can also use pre-defined templates for unit types:
    ```python
    from Template.UnitType import add_swordman
    elite_swordman_type = add_swordman(repo, name="Elite Swordman", hp=140, damage=18)
    ```

4.  **Add Units to the Game:** Place units on the map using `add_unit`, associating them with a `unit_type`, the game `map`, and the `player` who controls them.
    ```python
    from Logic.Unit import add_unit
    red_archer = add_unit(repo, archer_type.id, game.current_map.id, game.current_player.id, x=5, y=5) # Player 'Commander Red' gets an Archer
    blue_knight = add_unit(repo, knight_type.id, game.current_map.id, game.get_players(lambda p: p.name == "General Blue")[0].id, x=10, y=5) # 'General Blue' gets a Knight
    ```

5.  **Retrieve Game Objects:** Use the `repo.get()` method to retrieve objects from the repository, optionally filtering by type and conditions. For example, get all players in the current game:
    ```python
    from Logic.Player import get_players
    all_players = get_players(repo, game.id) # Get all players in the game
    blue_players = get_players(repo, game.id, condition=lambda player: player.name == "General Blue") # Get players named 'General Blue'
    ```

6.  **Draw the Map:** Visualize the game map at any time using `draw_map`.
    ```python
    from Logic.Map import draw_map
    draw_map(game.current_map.id, repo)
    ```

7.  **Saving and Loading Repository Data:** Persist your game state by saving the repository to a file, and load it later to continue your game.
    ```python
    repo.save("my_game_state", dir="saves") # Save the repository to 'saves/my_game_state.pkl'
    loaded_repo = Repo()
    loaded_repo.load("my_game_state", dir="saves") # Load the repository from 'saves/my_game_state.pkl'
    ```

Refer to the files within the `Logic` directory for a comprehensive view of available functions and features to interact with and expand upon the game engine.

## Project Structure

The Tactica project is structured to separate concerns and enhance maintainability:

*   **`Helper.py`**: Contains general utility functions used across the project, such as `generate_id()` for creating unique identifiers.
*   **`Repo.py`**: Defines the `Repo` class, implementing an in-memory repository for storing and retrieving game entities. It also handles saving and loading the repository to/from disk using pickle.
*   **`Logic/`**: This directory houses the core game logic and business rules.
    *   **`Game.py`**: Contains logic for game session management, including starting new games.
    *   **`Map.py`**: Logic for map-related operations, currently focused on drawing the map in text format.
    *   **`Player.py`**: Logic for player management, such as retrieving players associated with a game.
    *   **`Unit.py`**: Logic for unit management, including adding new units to the game world.
    *   **`UnitType.py`**: Logic for managing unit types, allowing the creation of new unit categories with specific attributes.
*   **`Model/`**: Defines the data models representing game entities. These classes define the structure and properties of game objects.
    *   **`Game.py`**: Model for the `Game` object, representing a game session.
    *   **`Map.py`**: Model for the `Map` object, defining the game world's grid.
    *   **`Player.py`**: Model for the `Player` object, representing a game player.
    *   **`Unit.py`**: Model for the `Unit` object, representing a game unit with position and type.
    *   **`UnitType.py`**: Model for the `UnitType` object, defining categories of units with shared characteristics.
*   **`Start.py`**:  The main script to start and demonstrate the Tactica engine. It sets up a basic game scenario and outputs the map to the console.
*   **`Template/`**: Contains template functions to quickly create pre-defined UnitTypes.
    *   **`UnitType.py`**: Includes functions like `add_infantry`, `add_swordman`, etc., to easily create common unit types.

---

**We hope you enjoy exploring and building tactical games with Tactica!**