import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals.loc[animals['weight'] > 100].sort_values(by = 'weight', ascending = False).drop(columns = ['species', 'age', 'weight'])
    return df