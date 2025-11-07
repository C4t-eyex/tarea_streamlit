import streamlit as st

def create_sliders( age_range_options: dict, hight_range_options: dict ):
    # Barra lateral ( aside )
    with st.sidebar:

        selected_age = st.slider(
            'Rango de Edad',
            min_value= age_range_options.get('min'),
            max_value= age_range_options.get('max'),
            step= 1,
            value=(age_range_options.get('min'), age_range_options.get('max'))
        )

        selected_height = st.slider(
            'Rango de Estatura (cm)',
            min_value= hight_range_options.get('min'),
            max_value= hight_range_options.get('max'),
            step= 1,
            value=(hight_range_options.get('min'), hight_range_options.get('max'))
        )

    return selected_age, selected_height