import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df = pd.melt(
        report, 
        id_vars = ['product'], 
        value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4']
        ).rename(columns = {'variable': 'quarter', 'value': 'sales'})
    # print(df.head())
    return df