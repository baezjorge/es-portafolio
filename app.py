from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Jorge Baez", page_icon=":computer:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Style/style.css")

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_49rdyysj.json")
tickets = Image.open("Images/tickets.png")
consolidado = Image.open("Images/consolidado.png")
ila = Image.open("Images/ila.png")
crm = Image.open("Images/crm.png")

with st.container():
    st.subheader("Hola, Soy Jorge Baez :wave:")
    st.title("Analista de Datos")
    st.write("Soy ingeniero de sistemas con enfasis en el análisis de datos e inteligencia de negocios para la toma de decisiones a través de Power BI, Excel, SQL y Python.")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Lo que ofrezco")
        st.write("##")
        st.write(
            """
            - Creación de tableros de alto nivel en Power BI.
            - Análisis exploratorio de datos a través de excel y python.
            - Recolección, integración y visualización de datos.
            - Validación de datos a través de Excel y SQL.
            - Creación y documentación de procesos.
            - Data storytelling.
            """ 
        )

    with right_column:
        st_lottie(lottie_coding, height=250, key="coding")

with st.container():
    st.write("---")
    st.header("Mis proyectos")
    st.write("#")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(tickets)


    with text_column:
        st.subheader("Tickets por día") 
        st.write(
            """
             Este proyecto muesta el comportamiento de los requerimientos a través de tickets. 
            Adicionalmente, se puede visualizar la distribución de días y horas con el objetivo de optimizar los recursos.
            """
        )
        st.markdown("[Click para ver el ejemplo](https://app.powerbi.com/view?r=eyJrIjoiMzdiYzE1ODctODEzMC00ZGU2LWE3ZTktMDNmN2JhYTNmNDAxIiwidCI6IjNkNmQwOGMxLWJlMzAtNDhjNy05NWQzLTI0NTA3MTQ4ZmQ0NCJ9)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(crm)


    with text_column:
        st.subheader("Gestión de relación con el cliente (CRM)") 
        st.write(
            """
           Este proyecto muestra información relevante obtenida desde un CRM. Podra visualizar e interactuar  con el presupuesto asignado vs. alcanzado, número de cotizaciones, leads, cierre de ventas, etc.
           Además, podra encontrar multiples segmentadores que le ayudaran a tener una mejor comprensión de la información desde los general hasta el detalle.
            """
        )   
        st.markdown("[Click para ver el ejemplo](https://app.powerbi.com/view?r=eyJrIjoiNDBhYjM5ZGQtYmE3Ny00MDk4LWE4Y2EtNjJjMjk4MzIxMjExIiwidCI6IjNkNmQwOGMxLWJlMzAtNDhjNy05NWQzLTI0NTA3MTQ4ZmQ0NCJ9)")


with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(consolidado)


    with text_column:
        st.subheader("Reporte de operaciones por zonas") 
        st.write(
            """
           Este proyecto muestra el comportamiento consolidado de las operaciones del servicio al cliente en salas de atención.
           Tiempo de atención y de espera sin mostrado para cada una de las oficinas.
            """
        )   
        st.markdown("[Click para ver el ejemplo](https://app.powerbi.com/view?r=eyJrIjoiNTIwMzVmYTctNWQxZC00ZDdkLTk4NjUtMTExODZkNjQ3MWYwIiwidCI6IjNkNmQwOGMxLWJlMzAtNDhjNy05NWQzLTI0NTA3MTQ4ZmQ0NCJ9)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(ila)


    with text_column:
        st.subheader("Impacto latinoamericano") 
        st.write(
            """
            Este proyecto fue realizado para una organización pro-eclesial. A través de el pordrá visualizar diferentes metricas en diferentes paises de Latinamérica. Incluye el detalle de la información para cada país y esta disponible en español e ingles.
            """
        )   
        st.markdown("[Click para ver el ejemplo](https://app.powerbi.com/view?r=eyJrIjoiNTkxMzE5MjEtZjBlYS00MmI3LWFhMDMtNjBiM2ZmMjkwYjFmIiwidCI6IjUxMWFjZTc5LTk0MjMtNGE1Ny1iMmEwLWM0Y2VjZDI4MmQxNiJ9)")        


with st.container():
    st.write("---")
    st.header("Contáctame")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/jorgebaez7@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Nombre" required>
     <input type="email" name="email"placeholder="Correo Electrónico" required>
     <textarea name = "message" placeholder "Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
