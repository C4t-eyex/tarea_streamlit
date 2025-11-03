from application.load_dataset import load_dataset
from application.remove_nulls import remove_nulls
from application.create_columns_1 import create_columns_1

def get_dataframe():
    df = load_dataset()
    df = remove_nulls( df )
    df = create_columns_1( df )

    return df