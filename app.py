import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.title("Menu lateral")

modulo  =  st.sidebar.selectbox("Elija un Acción",["Home","Ejercicio 01","Ejercicio 02","Ejercicio 03","Ejercicio 04"])

if modulo ==  "Home":
      col_img1, col_img2 = st.columns(2) 
            
      with col_img1:
          st.image("Python_logo.png", width=200)
            
      with col_img2:
          st.image("DMC.png", width=200)

      st.title("Trabajo Práctico Modulo 01")
      st.subheader("Oscar David Peñaherrera Cordova")
      st.write("Nombre del Modulo: Fundamentos de Phyton")
      st.write("Año:2026")
      st.write("Breve descripción del proyecto: Trabajo aplicativo")
      st.write("Tecnologías aplicadas: Google Colab, Streamlit y Github")

      
elif modulo == "Ejercicio 01":
      
      st.set_page_config(page_title="Ejercicio 01:Flujo de Caja")
      
      # 1. Inicializar la lista persistente en la sesión
      if "transacciones" not in st.session_state:
          st.session_state.transacciones = []
      
      st.title("Flujo de Caja")

      st.markdown("""
      Esta aplicación permite registrar transacciones de ingreso y salidas de dinero de una cuenta, detallando el historial y el saldo final.
      """)
      
      # 2. Entradas de datos con los componentes solicitados
      concepto = st.text_input("Concepto de la Transacción")
      tipo_movimiento = st.selectbox("Tipo de transacción", ["Ingreso", "Gasto"])
      valor = st.number_input("Valor (PEN)", min_value=0.0, step=1.0)
     
      
      # 3. Registro al hacer clic en el botón
      if st.button("Guardar Transacción"):
          if concepto.strip() == "":
              st.error("Por favor, escribe un concepto válido.")
          elif valor <= 0:
              st.error("El monto debe ser mayor a 0.")
          else:
              # Añadir la nueva transacción a la lista
              nueva_transaccion = {
                  "Concepto de la Transacción": concepto,
                  "Tipo de transacción": tipo_movimiento,
                  "Valor (PEN)": valor
                  
              }
              st.session_state.transacciones.append(nueva_transaccion)
              st.success(f"¡Transacción '{concepto}' registrada con éxito!")
      
      # 4. Mostrar resumen y visualización
      st.subheader("Resumen")
      
      if len(st.session_state.transacciones) > 0:
          df = pd.DataFrame(st.session_state.transacciones)
      
          # Cálculo de métricas
          ingresos = df[df["Tipo de transacción"] == "Ingreso"]["Valor (PEN)"].sum()
          gastos = df[df["Tipo de transacción"] == "Gasto"]["Valor (PEN)"].sum()
          balance = ingresos - gastos
      
          col1, col2, col3 = st.columns(3)
          col1.metric("Ingresos Total", f"${ingresos:.2f}")
          col2.metric("Gastos Total", f"${gastos:.2f}")
          col3.metric("Saldo", f"${balance:.2f}")
      
          # Visualizar la lista mediante dataframe
          st.dataframe(df, use_container_width=True)
      else:
          st.info("No hay transacciones en la lista.")    


   








