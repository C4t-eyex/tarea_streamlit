import streamlit as st
from presentation.show_title import title

st.set_page_config(
    page_title= title,
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)