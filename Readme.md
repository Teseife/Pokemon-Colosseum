# Pokemon Colosseum Game

## Overview
Pokemon Colosseum is a command-line game where the player battles against Team Rocket using Pokémon. Each side is assigned three random Pokémon, and the battle proceeds turn-by-turn until one team loses all its Pokémon. The player can choose moves for their Pokémon, while Team Rocket's moves are chosen randomly.

## Game Rules
- Both the player and Team Rocket start with three randomly selected Pokémon.
- Each Pokémon has a set of moves, HP, attack, and defense stats.
- A coin toss determines which team starts the battle.
- Moves deal damage based on factors such as attack, defense, type advantage, and random variability.
- The player cannot use the same move twice until all moves for that Pokémon have been used. Once all moves are used, the list resets.

## Features
- Dynamic move selection for the player with clear feedback on invalid choices.
- Resetting of moves once all are used.
- A damage calculation system based on Pokémon stats and type advantages.

## Prerequisites
- Python 3.11
- The following Python libraries:
  - `pandas`

## Files
1. **`Pokemon.py`**:
   - Contains the core classes and logic for Pokémon and move selection:
     - **`pokemon`**:
       - **`__init__(dfPkData, dfMvData, dfTypeMacthup)`**:
         - Parameters: DataFrames for Pokémon data, move data, and type matchups.
         - Initializes the class with all necessary game data.
       - **`teamPlayer()`**:
         - Parameters: None.
         - Randomly selects 3 Pokémon for the player's team.
         - Returns: List of Pokémon names (strings).
       - **`teamRocket()`**:
         - Parameters: None.
         - Randomly selects 3 Pokémon for Team Rocket.
         - Returns: List of Pokémon names (strings).
       - **`getmovesList(pokemonName)`**:
         - Parameters: Name of the Pokémon (string).
         - Retrieves the list of moves available for the specified Pokémon.
         - Returns: List of moves (strings).
       - **`Damage(Move, Attacker, Attacke)`**:
         - Parameters: Move name (string), attacker Pokémon (string), defender Pokémon (string).
         - Calculates the damage dealt by the specified move.
         - Returns: Damage value (int).
       - **`typeEfficiency(move, attacke)`**:
         - Parameters: Move name (string), defender Pokémon (string).
         - Determines the type effectiveness multiplier for the specified move.
         - Returns: Multiplier value (float).

     - **`selectors`**:
       - **`randomMove(moves)`**:
         - Parameters: List of moves (strings).
         - Randomly selects a move from the list, ensuring all moves are used before reshuffling.
         - Returns: Selected move (string).

2. **`PokemonColosseum.py`**:
   - Main game file that initializes the game and handles the battle logic.
   - Implements turn-based mechanics for the player and Team Rocket.
   - Tracks used moves and resets them when all moves are used.

3. **Data Files**:
   - **`pokemon-data.csv`**: Contains data about Pokémon (name, type, moves, stats).
   - **`moves-data.csv`**: Contains data about moves (name, type, power, etc.).


## Setting Up the Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game
To start the game, run the following command in the terminal:
```bash
python PokemonColosseum.py
```

## How to Play
1. Enter your name when prompted.
2. Your team of Pokémon and Team Rocket's Pokémon will be displayed.
3. Moves for each Pokémon are presented during the player's turn. Choose a move by entering its corresponding number.
4. Invalid inputs or moves marked as "N/a" will prompt a repick.
5. Battle continues until one team loses all its Pokémon.

## Example Gameplay
```plaintext
Welcome to Pokemon Colosseum!

Enter Player Name: Ash

Team Rocket enters with Gengar, Pikachu, and Charizard.

Team Ash enters with Bulbasaur, Squirtle, and Jigglypuff.

Let the battle begin!
Coin toss goes to ----- Team Rocket to start the attack!

Team Rocket's Gengar used Shadow Ball on Bulbasaur.
Damage to Bulbasaur is 40 points.
Bulbasaur has 60 HP remaining.

Choose the Move for Bulbasaur:
1) Vine Whip
2) Solar Beam
3) Razor Leaf
4) Take Down

Enter choice for Team Ash: 1
Bulbasaur used Vine Whip on Gengar.
Damage to Gengar is 30 points.
```

## Code Structure
- **`Pokemon.py`**:
  - Defines the `pokemon` class for managing Pokémon data and `selectors` class for move selection.
  - Key methods include:
    - `getmovesList(pokemonName)`: Returns the list of moves for a Pokémon.
    - `Damage(Move, Attacker, Attacke)`: Calculates the damage dealt by a move.
    - `typeEfficiency(move, attacke)`: Determines the type effectiveness of a move.

- **`PokemonColosseum.py`**:
  - Implements the game flow and turn-based battle system.
  - Tracks used moves and resets them when all moves are used.

