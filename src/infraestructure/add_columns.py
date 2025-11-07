import pandas as pd

def add_columns( df: pd.DataFrame ):

    # Columna Edad
    current_year = pd.Timestamp.now().normalize().year
    df = df.assign( Edad= lambda x:  current_year - x['Fecha_Nacimiento'].dt.year )

    # Estatura en Metros
    df['Estatura_M'] = df['Estatura'] / 100
    df.rename( columns={ 'Estatura': 'Estatura_CM' }, inplace=True )

    # Columna IMC
    df = df.assign( IMC= lambda x: x['Peso'] / ( ( x['Estatura_M'] ) ** 2 ) )

    # Clasificación IMC
    low_weight = df['IMC'] < 18.5
    adequate_weight = ( df['IMC'] >= 18.5 ) & ( df['IMC'] <= 24.9 )
    overweight = ( df['IMC'] >= 25 ) & ( df['IMC'] <= 29.9 )
    obesity_grade_1 = ( df['IMC'] >= 30 ) & ( df['IMC'] <= 34.9 )
    obesity_grade_2 = df['IMC'] >= 35

    df.loc[ low_weight, 'Clasificacion_IMC' ] = 'Bajo peso'
    df.loc[ adequate_weight, 'Clasificacion_IMC' ] = 'Adecuado'
    df.loc[ overweight, 'Clasificacion_IMC' ] = 'Sobrepeso'
    df.loc[ obesity_grade_1, 'Clasificacion_IMC' ] = 'Obesidad grado 1'
    df.loc[ obesity_grade_2, 'Clasificacion_IMC' ] = 'Obesidad grado 2'

    return df