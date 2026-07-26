import streamlit as st
import numpy as np

st.sidebar.title("Menu lateral")

modulo  =  st.sidebar.selectbox("Elija un Acción",["Home","Ejercicio 01","Ejercicio 02","Ejercicio 03","Ejercicio 04"])

if modulo ==  "Home":
      st.title("Trabajo Práctico Modulo 01")
      
      col_img1, col_img2 = st.columns(2) 
            
      with col_img1:
          st.image("Python_logo.png", width=250)
            
      with col_img2:
          st.image("DMC.png", width=250)

      st.subheader("Oscar David Peñaherrera Cordova")
      st.write("Nombre del Modulo: Fundamentos de Phyton")
      st.write("Año:2026")
      st.write("Breve descripción del proyecto: Trabajo aplicativo")
      st.write("Tecnologías aplicadas: Google Colab, Streamlit y Github")



   








