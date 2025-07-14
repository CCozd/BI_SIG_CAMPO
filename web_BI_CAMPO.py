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
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYmIyYTU1ZmUtNDg1Mi00NDcyLTk3MmQtMGVkODY2ZWQxNGZmIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('INVESTIGACIONES CIÉNTIFICAS EN CAMPO Y POSTCOSECHA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMGFhYzVkNWMtNDUwMi00NzFjLWFjOTAtNzkzOWI3YjAxMmFmIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('RENDIMIENTOS - SERVICIOS AGRÍCOLAS')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMTI3MTQ5NTktMWIyOC00MTdjLTg5NWItYTcwODYxZWI4ODI3IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('FERTIRRIEGO Y NUTRICIÓN')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNzhkMDE2ODYtNmYwNy00MGIyLWE5NzAtZDA1OWM4YTk5MjM3IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)



st.title('PROYECTO ARRIBOS')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZDMxMWUxNmEtMzAzYy00NzE4LTlkYjQtZjZiZTA0ZTZkZDI3IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)

st.title('COMITEE ARRIVAL')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYTA4YWU4MWQtYWJmMS00ZDMyLWJhOTMtMTVjZDY2ODU5YWUxIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('CLAIMS PROJECT')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYTliMWY1ZjctNDI1Yy00YWU1LTkxYjktZTdlMDYwMTYxODY5IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('UMBRALES ARRIBOS')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNTQ0Y2I4MDItZmE4ZS00YjdhLWFkOTMtM2YzYWU4MWI2N2NjIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('PRESUPUESTO GLOBAL')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYTI0NDc5NmYtZWQzNy00MWFjLWJhZjItY2M1ZTIzM2MyYzhlIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('PLANTA CHAO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiODg2MzljYmYtMmYxMC00NTQ1LThmMTYtZWNhNDIyYWMzMmE1IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('TODOS LOS CULTIVOS - PAISES')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYWE2MWMxNjYtYjAyOS00MmY5LTgyNGItY2U0YzI4NTM2YTlkIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('CAMPO - ARÁNDANO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZjg5MjM2ZjEtYWMzNC00ZmExLTkzMTYtZmE2ZjVhODQyZDJlIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('CAMPO PALTA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiY2YxNDFlNWItMzk3ZC00MzNkLTg1NmEtYTFlMzMxMjBkYjZkIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('MICROBIOLOGÍA - FRUTA CONGELADO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNjMxMjhkNWItOTU2MS00YmYzLTlmODgtOWM2ZTk4NDlhNTk0IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('ONE PAGE')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYWE2MWMxNjYtYjAyOS00MmY5LTgyNGItY2U0YzI4NTM2YTlkIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)


uploaded_pptx = st.file_uploader("Sube una presentación PowerPoint (.pptx)", type=["pptx"])

if uploaded_pptx is not None:
    presentation = Presentation(io.BytesIO(uploaded_pptx.read()))
    st.success(f"Archivo cargado: {uploaded_pptx.name}")
    
    for i, slide in enumerate(presentation.slides):
        st.subheader(f"🖼️ Diapositiva {i+1}")
        slide_text = ""
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                slide_text += shape.text.strip() + "\n"
        if slide_text.strip():
            st.text(slide_text.strip())
        else:
            st.info("Esta diapositiva no contiene texto.")
