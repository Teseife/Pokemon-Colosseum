
import pandas as pd

typeMatchUP = {
    "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1},
    "Fire": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 1, "Grass": 2},
    "Water": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 1, "Grass": 0.5},
    "Electric": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 0.5, "Grass": 0.5},
    "Grass": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5},
    "Other": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1},
}


dfTypeMacthup = pd.DataFrame(typeMatchUP).T

print(dfTypeMacthup.loc['Fire', 'Grass'])