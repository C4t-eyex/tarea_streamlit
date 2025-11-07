import pandas as pd

def get_sliders_options( df: pd.DataFrame ):
    age_range_options = {
        'min': int( df['Edad'].min() ),
        'max': int( df['Edad'].max() )
    }

    height_range_options = {
        'min': int( df['Estatura_CM'].min() ),
        'max': int( df['Estatura_CM'].max() )
    }

    return age_range_options, height_range_options