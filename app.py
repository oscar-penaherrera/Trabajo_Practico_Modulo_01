import streamlit as st
import numpy as np
import runpy

st.sidebar.title("Menu lateral")

modulo  =  st.sidebar.selectbox("Elija un Acción",["Home","Ejercicio 01","Ejercicio 02","Ejercicio 03","Ejercicio 04"])

if modulo ==  "Home":
           runpy.run_path("Home.py")
      
elif modulo == "Ejercicio 01":
  st.write("Estas en el módulo de Ejercicio 01")


   








