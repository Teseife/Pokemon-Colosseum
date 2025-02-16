from Pokemon import pokemon, selectors
import pandas as pd
import random


typeMatchUP = {
    "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1},
    "Fire": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 1, "Grass": 2},
    "Water": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 1, "Grass": 0.5},
    "Electric": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 0.5, "Grass": 0.5},
    "Grass": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5},
    "Other": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1},
}

dfTypeMacthup = pd.DataFrame(typeMatchUP).T
dfPkData = pd.read_csv('pokemon-data.csv')
dfMvData = pd.read_csv('moves-data.csv')

# Normalize this since I will not use these for anything.
dfMvData.drop(columns=["Category","Contest","PP","Accuracy"])
dfPkData.drop(columns=["height","weight"])

pokemonInstance = pokemon(dfPkData,dfMvData,dfTypeMacthup)

selector = selectors()

teamRocket = pokemonInstance.teamRocket()
teamPlayer = pokemonInstance.teamPlayer()

print("Welcome to Pokemon Colosseum! \n")

playerName = input("Enter Player Name: ")

print(f'Team Rocket enters with {", ".join(teamRocket)}. \n')

print(f'Team {playerName} enters with {", ".join(teamPlayer)}. \n')

players = ["TeamRocket",playerName]

winner = random.choice(players)

print(f"Let the battle begin!\nCoin toss goes to ----- {str(winner)} to start the attack! \n")

currentPlayer = winner
currentHP = {}

for pokemon in teamRocket:
    currentHP[pokemon] = pokemonInstance.getHP(pokemon)
for pokemon in teamPlayer:
    currentHP[pokemon] = pokemonInstance.getHP(pokemon)

chosen = {pokemon: set() for pokemon in teamPlayer + teamRocket}

# battle logic:
while True:
    if len(teamRocket) == 0:
        print(f"All of Team Rocket’s Pokémon fainted, and Team {playerName} prevails!")
        break
    elif len(teamPlayer) == 0:
        print(f"All of Team {playerName}'s Pokémon fainted, and Team Rocket prevails!")
        break

    teamRocketPK = teamRocket[0]
    playerPK = teamPlayer[0]

    if currentPlayer == 'TeamRocket':
        moves = pokemonInstance.getmovesList(teamRocketPK)
        randMove = selector.randomMove(moves)

        print(f"Team Rocket’s {teamRocketPK} cast {randMove} to {playerPK}:")
        damageTeamRocket = pokemonInstance.Damage(randMove, teamRocketPK, playerPK)
        print(f"Damage to {playerPK} is {damageTeamRocket} points")

        currentHP[playerPK] -= damageTeamRocket

        if currentHP[playerPK] <= 0:
            print(f"{playerPK} faints back to the poke ball.")
            teamPlayer.pop(0)
        else:
            print(f"{playerPK} has {currentHP[playerPK]} HP remaining.")
        currentPlayer = playerName
    else:
        print(f"Choose the Move for {playerPK}")
        playerMoves = pokemonInstance.getmovesList(playerPK) # list of moves

        availableMoves = []
        #moveMapping = []

        for move in playerMoves:
            if move in chosen[playerPK]:
                availableMoves.append(f"{move} N/a")
            else:
                availableMoves.append(move)
                #moveMapping.append(move)

        for index, move in enumerate(availableMoves):
            print(f"{index + 1}) {move}")


        while True:
            try:

                choice = int(input(f"Enter choice for Team {playerName}:")) - 1

                if choice < 0 or choice >= len(playerMoves):
                    raise IndexError

                chosenMove = playerMoves[choice]
                if availableMoves[choice].endswith("N/a"):
                    print("<<INVALID CHOICE>> You can't use the same move again until all moves are used!")
                    continue

                #choseMove = moveMapping[choice]
                print(f"{playerPK} cast {chosenMove} to {teamRocketPK}")
                chosen[playerPK].add(chosenMove)

                damageTeamPlayer = pokemonInstance.Damage(chosenMove, playerPK, teamRocketPK)
                print(f"Damage to {teamRocketPK} is {damageTeamPlayer} points")

                currentHP[teamRocketPK] -= damageTeamPlayer

                if currentHP[teamRocketPK] <= 0:
                    print(f"{teamRocketPK} faints back to the poke ball.")
                    teamRocket.pop(0)
                else:
                    print(f"{teamRocketPK} has {currentHP[teamRocketPK]} HP remaining.")
                currentPlayer = "TeamRocket"
                if len(chosen[playerPK]) == len(playerMoves):
                    print(f"All moves for {playerPK} have been used! Moves list is resetting.")
                    chosen[playerPK].clear()
                currentPlayer = "TeamRocket"
                break
            except(ValueError,IndexError):
                print("<<INVALID CHOICE>> You can only input numbers and choose form the available moves listed!")
                continue




