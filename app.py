import streamlit as st
import numpy as np

col_img1, col_img2 = st.columns(2) # Esto crea dos columnas de igual ancho

with col_img1:
    st.image("Python_logo.png", caption="Python Logo (Columna 1)", width=150)

with col_img2:
    st.image("DMC.png", caption="DMC Logo (Columna 2)", width=150)

st.write()
    
st.title("Trabajo Práctico Modulo 01")
st.subheader("Oscar David Penaherrera Cordova")






