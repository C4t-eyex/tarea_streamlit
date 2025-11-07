import pandas as pd

def get_metrics( filtered_data: pd.DataFrame ):
    students_total = filtered_data.shape[0]
    avg_age = filtered_data['Edad'].mean()
    avg_height = filtered_data['Estatura_CM'].mean()
    avg_weight = filtered_data['Peso'].mean()
    IMC = filtered_data['IMC'].mean()

    return {
        'students_total': students_total,
        'avg_age': avg_age,
        'avg_height': avg_height,
        'avg_weight': avg_weight,
        'IMC': IMC
    }