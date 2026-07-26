import streamlit as st
import numpy as np

col_left, col_rest = st.columns([1, 3]) # Columna pequeña a la izquierda, el resto del espacio a la derecha
with col_left:
    st.image("Python_logo.png",)

col_rest_right, col_right = st.columns([3, 1]) # El espacio restante a la izquierda, columna pequeña a la derecha
with col_right:
    st.image("DMC.png")
    
st.title("Trabajo Práctico Modulo 01")
st.subheader("Oscar David Penaherrera Cordova")






