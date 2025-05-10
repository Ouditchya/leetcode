import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset = ['email'], inplace = True)
    # customers.head(10)
    return customers