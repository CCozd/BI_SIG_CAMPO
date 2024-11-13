import streamlit as st

# Ocultar el menú de GitHub, opciones del menú, header y pie de página
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_link__1S137 {visibility: hidden;} /* Ocultar el texto "Hosted with Streamlit" */
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Títulos y visualización de los informes en iframes
frutas = {
    'ARÁNDANO': "https://app.powerbi.com/view?r=eyJrIjoiZjg5MjM2ZjEtYWMzNC00ZmExLTkzMTYtZmE2ZjVhODQyZDJlIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'UVA': "https://app.powerbi.com/view?r=eyJrIjoiZDA2ZjQyMmYtMWQxMy00ZmY1LTg0ZDMtZTIwODc5MmNlNmUxIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'MANDARINA': "https://app.powerbi.com/view?r=eyJrIjoiNjdhMzBlZWUtOWQwNS00YTI5LWIzNDEtMjM3OGQ1MWIwZGEyIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'PALTA': "https://app.powerbi.com/view?r=eyJrIjoiY2YxNDFlNWItMzk3ZC00MzNkLTg1NmEtYTFlMzMxMjBkYjZkIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'MANGO': "https://app.powerbi.com/view?r=eyJrIjoiNTUyYTJlYjAtNGViMC00OWRiLTkyMWUtYmMwOTBlOTYyYTBjIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'PITAHAYA': "https://app.powerbi.com/view?r=eyJrIjoiNWE4NmQzM2QtNWEzNi00NTYzLWFlOTEtNGVhMzZiZTU0MDhmIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'CAQUI': "https://app.powerbi.com/view?r=eyJrIjoiNzFlNWMxZTYtZGRiYy00M2Y3LWI2MTQtZGFlYjZlNDVkNGU3IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'LIMÓN': "https://app.powerbi.com/view?r=eyJrIjoiYzgxYWNiNDktZTExNi00NTE1LWI0ODAtOGY2MTgwODRiYjc1IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'INDICADOR BPAs': "https://app.powerbi.com/view?r=eyJrIjoiM2QwYmM2Y2ItYzUzNy00ZWRlLWFlZjYtOTNiMmFlZjNjZDVhIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'Evaluaciones fitosanitarias - MANGO': "https://app.powerbi.com/view?r=eyJrIjoiOTlhYzFhZWItZGE3Ny00ZmU5LTk4OTItOTRlNmM5MjIwZTQ4IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9",
    'Evaluaciones fitosanitarias - UVA': "https://app.powerbi.com/view?r=eyJrIjoiMWEyNWEyZjktNDJmMC00ZWVhLWE5MzItMjM3ZWNmYjQzMzBiIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9"
}

for fruta, url in frutas.items():
    st.title(fruta)
    st.components.v1.iframe(url, height=600)
