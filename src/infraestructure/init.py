from infraestructure.load_dataset import load_dataset
from infraestructure.add_columns import add_columns
from infraestructure.pre_process_data import pre_process_data

def get_dataframe():
    df = load_dataset()
    modified_df = add_columns( df )
    cleaned_df = pre_process_data( modified_df )

    return cleaned_df