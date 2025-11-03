import pandas as pd

def remove_nulls( df: pd.DataFrame ):
    df.dropna( inplace=True )
    
    return df
