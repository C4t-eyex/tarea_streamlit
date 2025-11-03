import pandas as pd

def create_columns_1( df: pd.DataFrame ):

    # Columna Edad
    current_year = pd.Timestamp.now().normalize().year
    df = df.assign( Edad= lambda x:  current_year - x['Fecha_Nacimiento'].dt.year, )

    # Columna
    # dataset = dataset.assign( Edad= lambda x:  current_year - x['Fecha_Nacimiento'].dt.year, )

    return df