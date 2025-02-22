# Tactica - Python Tactical Game Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Tactica** is a simple Python-based engine for creating turn-based tactical games. It provides a foundation for game logic, map management, player and unit handling, and a basic in-memory repository for game data. This project is in its early stages and serves as a starting point for building more complex tactical game systems.

## Key Features

*   **Game Management:** Create and manage game instances, define game names, and track the current game state.
*   **Map Generation:**  Define map sizes and represent game maps as grid-based environments.
*   **Player Management:**  Add and manage players within a game, assigning names and tracking the current player.
*   **Unit Types and Units:** Define different unit types with attributes like health, damage, and range, and create individual units placed on the game map, owned by players.
*   **In-Memory Repository:** Utilizes a simple repository pattern for storing and retrieving game objects (Games, Maps, Players, Units, Unit Types) without external database dependencies, ideal for prototyping and small-scale projects.
*   **Basic Map Drawing:**  Provides a text-based visualization of the game map in the console, showing unit positions.

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

To see Tactica in action, run the `Start.py` file. This script initializes a game, adds unit types and units, and draws a representation of the game map in your console.

```bash
python Start.py
```

You should see output in your console representing the game map with units placed on it.

## Usage

The `Start.py` file provides a basic example of how to use the Tactica engine. Here's a breakdown of the key components and how you might use them:

1.  **Initialize the Repository:** Create an instance of the `Repo` class to manage game objects.
    ```python
    repo = Repo()
    ```

2.  **Start a New Game:** Use the `start_game` function to create a new game instance, define the map size, and add players.
    ```python
    game = start_game(repo, "My New Game", 15, 8, ["Player One", "Player Two"])
    ```

3.  **Define Unit Types:**  Use `add_unit_type` to create different types of units with specific attributes.
    ```python
    archer_type = add_unit_type(repo, "Archer", hp=70, is_ranged=True, damage=15)
    ```

4.  **Add Units to the Game:** Use `add_unit` to place units on the map, associating them with a unit type, map, and player.
    ```python
    player1_unit = add_unit(repo, archer_type.id, game.current_map.id, game.current_player.id, x=3, y=4)
    ```

5.  **Draw the Map:**  Use `draw_map` to visualize the current game map in the console.
    ```python
    draw_map(game.current_map.id, repo)
    ```

Refer to the files in the `Logic` directory for more functions and capabilities to interact with the game engine.

## Project Structure

The Tactica project is organized into the following directories and files:

*   **`Helper.py`**: Contains utility functions, currently just `generate_id()` for creating unique identifiers for game objects.
*   **`Repo.py`**: Defines the `Repo` class, a simple in-memory repository for storing and retrieving game entities.
*   **`Logic/`**: Contains the business logic of the game engine.
    *   **`Game.py`**: Logic related to game management (starting games).
    *   **`Map.py`**: Logic for map operations (drawing maps).
    *   **`Player.py`**: Logic for player management (retrieving players).
    *   **`Unit.py`**: Logic for unit management (adding units).
    *   **`UnitType.py`**: Logic for unit type management (adding unit types).
*   **`Model/`**: Defines the data models for the game entities.
    *   **`Game.py`**: Model for the `Game` object.
    *   **`Map.py`**: Model for the `Map` object.
    *   **`Player.py`**: Model for the `Player` object.
    *   **`Unit.py`**: Model for the `Unit` object.
    *   **`UnitType.py`**: Model for the `UnitType` object.
*   **`Start.py`**: A script that demonstrates how to use the Tactica engine by setting up and running a basic game example.

---

**Enjoy building your tactical games with Tactica!**
