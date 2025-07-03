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

st.title('IMPACTOS ECONÓMICOS - CALIDAD')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZDM0YjlmNTUtODU4MC00ZGE1LWE3YzktNzJlM2Q3NWFhMjQ1IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('PREDICCIÓN EVENTOS CLIMATICOS')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMGQzYzA2MjUtNDcxZS00ZjhjLTlkYjYtYmNhYmU4ZmM2YTI3IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('PREDICCIÓN DESARROLLO FLORAL ')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYzQxZTQ1YzgtYjU3Ni00MjhkLTkyNjEtZGVmZWMzZDVlN2ZlIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('INDICE DE BALANCE - PALTA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZDg3MzRkMWItYWFjNy00NDQ2LTg5ZDUtNWQyOGZmMjAxNGEwIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('INDICE DE BALANCE - ARÁNDANO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMDc0OTFjM2UtZTBhZi00ZjhjLTkwNDEtNWZhZjFiMjViNjYxIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('INDICE DE BALANCE - MANGO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZmRiMzMzZWQtOWY3NC00MzRkLWIwZmQtMGYwNzE5NzAzZWU3IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('ANÁLISIS FENOLÓGICOS')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMzg0M2E0MTgtMzUyYi00OTVmLTg5MjItYzg3NWEwNjE5Y2VmIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
