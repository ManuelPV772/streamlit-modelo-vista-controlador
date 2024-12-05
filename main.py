import streamlit as st
from modelo import Modelo
from vista import Vista
from controlador import Controlador

# Crear conexión a la base de datos
conn = st.connection("user_data_db", type="sql")

# Crear tabla si no existe
with conn.session as s:
    s.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        );
        """
    )
    s.commit()

# Inicializar las clases
modelo = Modelo(conn)
vista = Vista()
controlador = Controlador(modelo, vista)

# Ejecutar la aplicación
controlador.ejecutar()