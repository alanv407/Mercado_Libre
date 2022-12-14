#Librerias
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

#Configurarci贸n P谩ginas
st.set_page_config(
	page_title = 'Caso Mercado Libre',
	page_icon = '馃洅',
	)

st.title('***Alan Arturo Vargas Andrade***')
st.title('Sobre Mi')

with st.expander("Saber un poco m谩s"):
    st.write("""
        Soy el tipo de persona que no le teme a los desaf铆os, me gusta aportar innovaci贸n y motivaci贸n al equipo de trabajo. \n 
        Me describo como una persona din谩mica, anal铆tica, con gran facilidad para aprender y orientado a resultados. \n
    """)


st.header('Experiencia Profesional')

with st.expander("Saber un poco m谩s"):
    st.write("""
        Cuento con experiencia en manipulaci贸n e interpretaci贸n de datos. \n 
        Las herramientas que m谩s uso son; SQL, Power BI, Python y Excel.
    """)

st.header('Empleos Anteriores')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["IQVIA", "Rappi", "MexW眉rst", "Wonder World Media",'Antoeli'])

with tab1:
   st.subheader("Data Analyst")
   st.caption('2021 - presente')
   st.markdown('- Uso de bases de datos (SSIS, SQL, Access)')
   st.markdown('- Automatizaci贸n de movimientos de datos y transformaci贸n de los mismos, ETL (Extraction, Transformation and Load)')
   st.markdown('- Implementaci贸n de soluciones de BI')
   st.markdown('- Extracci贸n y transformaci贸n de datos Sell Out Sell In')
   st.markdown('- An谩lisis de la integridad de la Base de Datos')
   st.markdown('- An谩lisis y dise帽o de reportes para direcci贸n general y clientes')
   #st.markdown('')
with tab2:
   st.subheader("Analista Retail CPG麓s")
   st.caption('2019 - 2020')
   st.markdown('- Implementaci贸n de metodolog铆a Agile Scrum(reducci贸n de backlog, tiempo de finalizaci贸n y entrega de tareas, reducci贸n de errores en promociones)')
   st.markdown('- Montaje de tiendas, productos y precios en aplicaci贸n y Web (CMS)')
   st.markdown('- Actualizaci贸n y depuraci贸n de base de datos (SQL)')
   st.markdown('- Implementaci贸n de nuevos procesos internos dentro de la aplicaci贸n con el 谩rea Tech')

with tab3:
   st.subheader("Especialista en Marketing")
   st.caption('2018 - 2019')
   st.markdown('- An谩lisis de portafolio de productos')
   st.markdown('- An谩lisis econ贸mico, financiero y operaciones')
   st.markdown('- Direcci贸n del cambio de la imagen corporativa' )
   st.markdown('- Creaci贸n e implementaci贸n de estrateg铆a de marketing (Web, SEO, SEM y app)')

with tab4:
   st.subheader("Internship 馃嚜馃嚫")
   st.caption('2017 - 2018')
   st.markdown('- Pr谩cticas profesionales en Espa帽a en el 谩rea de gesti贸n comercial y marketing digital.')
   st.markdown('- B煤squeda de mercados no cubiertos en el 谩rea metropolitana de Barcelona')
   st.markdown('- Dise帽o e implementaci贸n de estrategias de marketing digital (RRSS, Web, e-commerce, tradicional)')
   st.markdown('- Organizaci贸n y planificaci贸n de eventos corporativos')

with tab5:
   st.subheader("Asesor de Ventas")
   st.caption('2017')
   st.markdown('- Orientaci贸n y asesor铆a al cliente en la elecci贸n del equipo adecuado a sus necesidades, brindando demostraciones pre-venta, para una elecci贸n adecuada conforme a lo requerido.')
   st.markdown('- Detecci贸n de necesidades espec铆ficas del cliente, generando confianza y satisfacci贸n, incluyendo dentro del proceso de venta la asesor铆a de los requerimientos de instalaci贸n y mantenimiento, en la post-venta manteniendo contacto al cliente verificando la satisfacci贸n y seguimiento de sus necesidades')

st.header('Educaci贸n')
tab5, tab6, tab7 = st.tabs(['M谩ster Universitario 馃嚜馃嚫','Licenciatura 馃嚥馃嚱','Diploma'])

with tab5:
	st.subheader('Direcci贸n de Marketing y Gesti贸n Comercial')
	st.markdown('EAE BUSINESS SCHOOL / UNIVERSITAT POLIT脠CNICA DE CATALUNYA')
	st.caption('2017 - 2018')

with tab6:
	st.subheader('Qu铆mica')
	st.markdown('Universidad La Salle')
	st.caption('2012 - 2016')

with tab7:
	st.subheader('Big Data')
	st.markdown('Fundaci贸n Carlos Slim / SEP')
	st.caption('527 horas / 2021')







