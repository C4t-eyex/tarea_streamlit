import streamlit as st

def show_metrics( params: dict ):

    # Mostramos las métricas
    # Declaramos 5 columnas de igual tamaño
    c1, c2, c3, c4, c5 = st.columns( 5 )

    with c1:
        st.metric(label='Total Estudiantes', value=params.get('students_total'), border=True)
    
    with c2:
        st.metric(label='Edad Promedio', value=f'{params.get('avg_age'):,.0f}', border=True)
    
    with c3:
        st.metric(label='Estatura Promedio', value=f'{params.get('avg_height'):,.0f}', delta='CM', border=True)
    
    with c4:
        st.metric(label='Peso Promedio', value=f'{params.get('avg_weight'):,.0f}', delta='KG', border=True)
    
    with c5:
        st.metric(f'IMC Promedio', f'{params.get('IMC'):,.0f}', border=True)