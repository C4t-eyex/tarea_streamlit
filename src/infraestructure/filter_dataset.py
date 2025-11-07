import pandas as pd

def filter_dataset( params: dict, df: pd.DataFrame ):
    filtered_data = df

    if params.get('selected_students').shape[0] > 0:
        filtered_data = filtered_data[ filtered_data['Código'].isin( params.get('selected_students') ) ]

    if params.get('selected_blood_type'):
        filtered_data = filtered_data[ filtered_data['RH'].isin( params.get('selected_blood_type') ) ]

    if params.get('selected_hair_color'):
        filtered_data = filtered_data[ filtered_data['Color_Cabello'].isin( params.get('selected_hair_color') ) ]

    if params.get('selected_neightborhood'):
        filtered_data = filtered_data[ filtered_data['Barrio_Residencia'].isin( params.get('selected_neightborhood') ) ]

    if params.get('selected_age'):
        min_age = params.get('selected_age')[0]
        max_age = params.get('selected_age')[1]
        filtered_data = filtered_data[ ( filtered_data['Edad'] >= min_age ) & ( filtered_data['Edad'] <= max_age ) ]
    
    if params.get('selected_height'):
        min_height = params.get('selected_height')[0]
        max_height = params.get('selected_height')[1]
        filtered_data = filtered_data[ ( filtered_data['Estatura_CM'] >= min_height ) & ( filtered_data['Estatura_CM'] <= max_height ) ]
    
    return filtered_data