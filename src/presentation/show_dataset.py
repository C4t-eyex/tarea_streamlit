import streamlit as st
import pandas as pd

def show_dataset( df: pd.DataFrame ):
    st.dataframe( df )