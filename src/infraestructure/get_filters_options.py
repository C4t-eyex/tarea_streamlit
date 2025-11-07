import pandas as pd

students = ['ALEJANDRO GIRALDO OCAMPO', 'MARCOS DUQUE JARAMILLO', 'YEFERSON SERNA RESTREPO', 'CAMILO RODRIGUEZ GOMEZ']

def get_filters_options( df: pd.DataFrame ):

    df['Nombre_Completo_Estudiante'] = df['Nombre_Estudiante'].astype(str) + ' ' + df['Apellido_Estudiante'].astype(str)
    is_student_option = df['Nombre_Completo_Estudiante'].isin( students )

    student_options = {
        'code': df[ is_student_option ]['Código'].to_numpy(),
        'full_name': df[ is_student_option ]['Nombre_Completo_Estudiante'].to_numpy()
    }

    blood_type_options = df['RH'].unique()
    hair_color_options = df['Color_Cabello'].unique()
    neightborhood_options = df['Barrio_Residencia'].unique()

    return student_options, blood_type_options, hair_color_options, neightborhood_options