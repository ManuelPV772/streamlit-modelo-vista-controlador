import streamlit as st
import sqlalchemy

from modelo import Modelo
from vista import Vista
from controlador import Controlador

# Crear conexión a la base de datos
conn = st.connection("user_data_db", type="sql")

table = sqlalchemy.sql.text(
            "CREATE TABLE IF NOT EXISTS users "
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "name TEXT NOT NULL, "
            "age INTEGER NOT NULL)"
        )
conn.session.execute(table);

# Inicializar las clases
modelo = Modelo(conn)
vista = Vista()
controlador = Controlador(modelo, vista)

# Ejecutar la aplicación
controlador.ejecutar()
