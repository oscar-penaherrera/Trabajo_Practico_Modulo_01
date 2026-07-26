import streamlit as st
import numpy as np

# Esto crea dos columnas de igual ancho
col_img1, col_img2 = st.columns(2) 

with col_img1:
    st.image("Python_logo.png", width=250)

with col_img2:
    st.image("DMC.png", width=250)

st.write()
    
st.title("Trabajo Práctico Modulo 01")
st.subheader("Oscar David Penaherrera Cordova")






