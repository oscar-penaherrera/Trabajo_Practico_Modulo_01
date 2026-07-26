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
      Para esto, se debe completar el formulario y luego seleccionar **Guardar Transacción**.
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

elif modulo == "Ejercicio 02":

      # Configuración inicial de la página
      st.set_page_config(page_title="Ejercicio 02: Formulario para registro de información")
      
      # 1. Inicializar los arrays de NumPy en st.session_state si no existen
      if "nombres" not in st.session_state:
          st.session_state.nombres = np.array([], dtype=str)
          st.session_state.categorias = np.array([], dtype=str)
          st.session_state.precios = np.array([], dtype=float)
          st.session_state.cantidades = np.array([], dtype=int)
          st.session_state.totales = np.array([], dtype=float)
      
      # Título de la aplicación
      st.title("Registro de Productos")
      
      # Descripción del ejercicio usando st.markdown()
      st.markdown("""
      Esta aplicación permite registrar información de diferntes productos. 
      Una vez completados los campos, al presionar el botón **Agregar Producto**, los datos ingresados en el formulario se almacenan 
       y luego se consolidaran en la tabla inferior.
      """)
      
      st.divider()
      
      # Formulario de ingreso de datos con los widgets recomendados
      st.subheader("Formulario de Ingreso")
      
      nombre = st.text_input("Nombre del producto")
      categoria = st.selectbox(
          "Categoría", ["Electrónica", "Abarrotes", "Ropa", "Hogar", "Otros"]
      )
      precio = st.number_input("Precio unitario (PEN)", min_value=0.0, step=0.50)
      cantidad = st.number_input("Cantidad", min_value=1, step=1)
      
      # Botón para agregar un nuevo registro
      if st.button("Agregar Producto"):
          if nombre.strip() == "":
              st.error("Por favor, ingresa el nombre del producto.")
          elif precio <= 0:
              st.error("El precio debe ser mayor a 0.")
          else:
              # Cálculo del total
              total = precio * cantidad
      
              # Agregar los nuevos elementos a los arrays usando np.append()
              st.session_state.nombres = np.append(st.session_state.nombres, nombre)
              st.session_state.categorias = np.append(
                  st.session_state.categorias, categoria
              )
              st.session_state.precios = np.append(st.session_state.precios, precio)
              st.session_state.cantidades = np.append(
                  st.session_state.cantidades, cantidad
              )
              st.session_state.totales = np.append(st.session_state.totales, total)
      
              st.success(f"¡Producto **'{nombre}'** agregado correctamente!")
      
      # Sección de visualización de datos
      st.subheader("Tabla de Productos Registrados")
      
      # Verificar si hay elementos almacenados en el array de NumPy
      if len(st.session_state.nombres) > 0:
          # Convertir los arrays de NumPy en un DataFrame de Pandas
          datos = {
              "Nombre del Producto": st.session_state.nombres,
              "Categoría": st.session_state.categorias,
              "Precio (PEN)": st.session_state.precios,
              "Cantidad": st.session_state.cantidades,
              "Total (PEN)": st.session_state.totales,
          }
      
          df_productos = pd.DataFrame(datos)
      
          # Mostrar la tabla en pantalla
          st.dataframe(df_productos, use_container_width=True)
      
          # Opcional: Métricas acumuladas usando funciones de NumPy (np.sum)
          gran_total = np.sum(st.session_state.totales)
          total_unidades = np.sum(st.session_state.cantidades)
      
          col1, col2 = st.columns(2)
          col1.metric("Total de Unidades", f"{total_unidades} unds.")
          col2.metric("Monto Total Acumulado", f"S/ {gran_total:.2f}")
      
      else:
          st.info("No hay productos registrados en la matriz de NumPy.")

elif modulo == "Ejercicio 03":
   
      # ---------------------------------------------------------
      # 1. Importar funciones
      # ---------------------------------------------------------
      
      from libreria_funciones_proyecto1.py import calcular_rotacion_inventario
      
      # Título de la aplicación
      st.title("Función desde Librería Externa: **Rotación de Inventarios**")
      # ---------------------------------------------------------
      # INICIALIZACIÓN DEL HISTORIAL (st.session_state)
      # ---------------------------------------------------------
      if "historico" not in st.session_state:
          # Creamos un DataFrame vacío para almacenar los resultados
          st.session_state.historico = pd.DataFrame(
              columns=["Función", "Parámetros", "Resultado"]
          )
      
      # ---------------------------------------------------------
      # INTERFAZ Y WIDGETS DE STREAMLIT
      # ---------------------------------------------------------
      st.title(" Aplicación Multitarea - Streamlit")
      st.write("Selecciona una función, ingresa los parámetros requeridos y guarda los resultados.")
      
      # Widget 1: Selector de función
      funcion_seleccionada = st.selectbox(
          "1. Selecciona la función a ejecutar:",
          ("Calculadora de Descuentos", "Cálculo de Interés Simple")
      )
      
      st.divider()
      
      # Widgets dinámicos según la función seleccionada
      if funcion_seleccionada == "Calculadora de Descuentos":
          st.subheader("Parámetros: Descuento")
          
          # Widgets 2 y 3: Entradas numéricas
          precio_input = st.number_input("Precio original ($):", min_value=0.0, value=100.0, step=10.0)
          descuento_input = st.number_input("Porcentaje de descuento (%):", min_value=0.0, max_value=100.0, value=15.0)
          
          # Widget 4: Botón para ejecutar
          if st.button("Ejecutar y Guardar"):
              resultado = calcular_descuento(precio_input, descuento_input)
              
              # Widget 5: Mostrar resultado en pantalla
              st.success(f"**Resultado:** El precio con descuento es **${resultado:.2f}**")
              
              # 6. Guardar en el histórico
              nuevo_registro = {
                  "Función": funcion_seleccionada,
                  "Parámetros": f"Precio: ${precio_input}, Desc: {descuento_input}%",
                  "Resultado": f"${resultado:.2f}"
              }
              # Añadir la nueva fila al DataFrame guardado en la sesión
              st.session_state.historico = pd.concat(
                  [st.session_state.historico, pd.DataFrame([nuevo_registro])],
                  ignore_index=True
              )
      
      elif funcion_seleccionada == "Cálculo de Interés Simple":
          st.subheader("Parámetros: Interés Simple")
          
          capital_input = st.number_input("Capital inicial ($):", min_value=0.0, value=1000.0, step=100.0)
          tasa_input = st.number_input("Tasa de interés anual (%):", min_value=0.0, value=5.0, step=0.5)
          tiempo_input = st.number_input("Tiempo (años):", min_value=0.0, value=1.0, step=0.5)
          
          if st.button("Ejecutar y Guardar"):
              resultado = calcular_interes_simple(capital_input, tasa_input, tiempo_input)
              
              st.success(f"**Resultado:** El interés generado es de **${resultado:.2f}**")
              
              nuevo_registro = {
                  "Función": funcion_seleccionada,
                  "Parámetros": f"Capital: ${capital_input}, Tasa: {tasa_input}%, Años: {tiempo_input}",
                  "Resultado": f"${resultado:.2f}"
              }
              st.session_state.historico = pd.concat(
                  [st.session_state.historico, pd.DataFrame([nuevo_registro])],
                  ignore_index=True
              )
      
            # ---------------------------------------------------------
            # MUESTRA DEL HISTÓRICO
            # ---------------------------------------------------------
            st.divider()
            st.subheader(" Tabla Histórica de Resultados")
            
            # Widget 6: Mostrar el DataFrame en pantalla
            st.dataframe(st.session_state.historico, use_container_width=True)
            
            # Opción adicional: Limpiar el historial
            if not st.session_state.historico.empty:
                if st.button("Limpiar Historial"):
                    st.session_state.historico = pd.DataFrame(columns=["Función", "Parámetros", "Resultado"])
                    st.rerun()
      
      
      
      
      
      
