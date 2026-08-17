import pandas as pd

def findHeavyAnimals(df: pd.DataFrame) -> pd.DataFrame:
    res=(
        df.dropna(subset=['weight'])
        .query('weight > 100').
        sort_values(by='weight',ascending=False)
        [['name']]
    )
    return res.reset_index(drop=True)