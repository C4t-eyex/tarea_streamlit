import streamlit as st

def create_multiselect_filters( student_options, blood_type_options, hair_color_options, neightborhood_options ):
    # Barra lateral ( aside )
    with st.sidebar:

        selected_blood_types = st.multiselect(
            'Tipo de Sangre (RH)', 
            options=blood_type_options,
            placeholder='Selecciona el Tipo'
        )

        selected_hair_colors = st.multiselect(
            'Color de Cabello', 
            options=hair_color_options,
            placeholder='Selecciona el Color'
        )

        selected_neightborhoods = st.multiselect(
            'Barrio de Residencia', 
            options=neightborhood_options, 
            placeholder='Selecciona la Residencia'
        )
        
        selected_students = st.multiselect(
            'Estudiantes', 
            options=student_options, 
            placeholder='Selecciona a un Estudiante'
        )

    return selected_students, selected_blood_types, selected_hair_colors, selected_neightborhoods