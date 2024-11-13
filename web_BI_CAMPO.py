import streamlit as st

# Ocultar el menú de GitHub y otras opciones
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Ocultar el pie de página "Hosted with Streamlit"
hide_footer_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)


st.title('ARÁNDANO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZjg5MjM2ZjEtYWMzNC00ZmExLTkzMTYtZmE2ZjVhODQyZDJlIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('UVA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZDA2ZjQyMmYtMWQxMy00ZmY1LTg0ZDMtZTIwODc5MmNlNmUxIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('MANDARINA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNjdhMzBlZWUtOWQwNS00YTI5LWIzNDEtMjM3OGQ1MWIwZGEyIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('PALTA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiY2YxNDFlNWItMzk3ZC00MzNkLTg1NmEtYTFlMzMxMjBkYjZkIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('MANGO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNTUyYTJlYjAtNGViMC00OWRiLTkyMWUtYmMwOTBlOTYyYTBjIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('PITAHAYA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNWE4NmQzM2QtNWEzNi00NTYzLWFlOTEtNGVhMzZiZTU0MDhmIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('CAQUI')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNzFlNWMxZTYtZGRiYy00M2Y3LWI2MTQtZGFlYjZlNDVkNGU3IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('LIMÓN')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYzgxYWNiNDktZTExNi00NTE1LWI0ODAtOGY2MTgwODRiYjc1IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('INDICADOR BPAs')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiM2QwYmM2Y2ItYzUzNy00ZWRlLWFlZjYtOTNiMmFlZjNjZDVhIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('Evaluaciones fitosanitarias - MANGO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOTlhYzFhZWItZGE3Ny00ZmU5LTk4OTItOTRlNmM5MjIwZTQ4IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('Evaluaciones fitosanitarias - UVA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMWEyNWEyZjktNDJmMC00ZWVhLWE5MzItMjM3ZWNmYjQzMzBiIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
