import pandas as pd

def load_dataset():
    file_url = './dataset/ListadoDeEstudiantesGrupo_050.xlsx'

    return pd.read_excel( file_url )