import pandas as pd

def pre_process_data( df: pd.DataFrame ):

    # Eliminamos las filas con campos nulos
    df = remove_nulls( df )

    # Removemos espacios y convertimos el campo Tipo de Sangre a formato mayuscula
    df['RH'] = df['RH'].str.replace(' ', '')
    df['RH'] = df['RH'].str.upper()

    # Convertimos el campo Color de Cabello a formatato title case
    df['Color_Cabello'] = df['Color_Cabello'].str.title()

    # Convertimos el campo Barrio Residencia a formatato title case
    df['Barrio_Residencia'] = df['Barrio_Residencia'].str.title()

    # Removemos espacios en los campos Nombre y Apellido del estudiante
    df['Nombre_Estudiante'] = df['Nombre_Estudiante'].str.strip()
    df['Apellido_Estudiante'] = df['Apellido_Estudiante'].str.strip()

    return df

def remove_nulls( df: pd.DataFrame ):
    df.dropna( inplace=True )
    
    return df