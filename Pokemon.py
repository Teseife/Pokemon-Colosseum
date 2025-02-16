import random
import ast


class pokemon:
    def __init__(self, dfPkData, dfMvData, dfTypeMacthup):
        self.dfPk = dfPkData
        self.dfMv = dfMvData
        self.dfTM = dfTypeMacthup

    def teamPlayer(self):
        pokemons = self.dfPk.sample(n=3)['Name'].tolist()
        return pokemons

    def teamRocket(self):
        pokemons = self.dfPk.sample(n=3)['Name'].tolist()
        return pokemons

    def getmovesList(self, pokemonName):
        # goes through the 'Name' column of the Pokemon-csv file checks if the parameter is true and returns the moves in a list format.
        moves = self.dfPk.loc[self.dfPk['Name'] == pokemonName, 'Moves'].iloc[0]
        return ast.literal_eval(moves)

    def getHP(self, pokemonName):
        HP = self.dfPk.loc[self.dfPk['Name'] == pokemonName, 'HP'].iloc[0]
        return HP

    def moveType(self, move):
        type = self.dfMv.loc[self.dfMv['Name'] == move, 'Type'].iloc[0]
        return type

    def pokemoneType(self, pokemoneName):
        type = self.dfPk.loc[self.dfPk['Name'] == pokemoneName, 'Type'].iloc[0]
        return type

    def movePower(self, move):
        # goes through the 'Name' column in the moves-csv file and returns the power of the move.
        powerPts = self.dfMv.loc[self.dfMv['Name'] == move, 'Power'].iloc[0]
        return powerPts

    def pokemonAttack(self, pokemonName):
        attackPts = self.dfPk.loc[self.dfPk['Name'] == pokemonName, 'Attack'].iloc[0]
        return attackPts

    def pokemonDefense(self, pokemonName):
        defensePts = self.dfPk.loc[self.dfPk['Name'] == pokemonName, 'Defense'].iloc[0]
        return defensePts

    # Same Type Attack Bonus IF attck type macths with pokemon type retun 1.5 else 1

    def STAB(self, pokemonName, move):
        moveType = self.dfMv.loc[self.dfMv['Name'] == move, 'Type'].iloc[0]
        pokemonType = self.dfPk.loc[self.dfPk['Name'] == pokemonName, 'Type'].iloc[0]
        if pokemonType == moveType:
            return 1.5
        else:
            return 1

    def typeEfficiency(self, move, attacke):

        moveType = self.moveType(move)
        attackeType = self.pokemoneType(attacke)

        # moveType = moveType.capitalize()
        # attackeType = attackeType.capitalize()

        if moveType not in self.dfTM:
            moveType = 'Other'

        value = self.dfTM.loc[moveType, attackeType]
        return value

    '''
    For for the move Type I need to make a private method that can retrive, the move type of a given move
    and then take the attacke's form the Damage function and put it as a parameter as well.
    '''

    def Damage(self, Move, Attacker, Attacke):
        power = self.movePower(Move)
        attack = self.pokemonAttack(Attacker)
        defense = self.pokemonDefense(Attacke)
        STAB = self.STAB(Attacker, Move)
        TE = self.typeEfficiency(Move, Attacke)
        Random = random.uniform(0.5, 1)
        # print(f"")
        damage = power * (attack / defense) * STAB * TE * Random
        return round(damage)


class selectors:
    def __init__(self):
        self.remainingItems = []

    def randomMove(self, moves):
        if not self.remainingItems:
            self.remainingItems = moves.copy()
            random.shuffle(self.remainingItems)
        return self.remainingItems.pop()
