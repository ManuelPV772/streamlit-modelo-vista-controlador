import streamlit as st

class Vista:
    def mostrar_titulo(self):
        st.title("Gestión de Usuarios")

    def mostrar_formulario(self):
        name = st.text_input("Nombre:")
        age = st.number_input("Edad:", min_value=1, step=1)
        guardar_presionado = st.button("Guardar")  # Botón está aquí, en la Vista
        return name, age, guardar_presionado

    def mostrar_mensaje(self, mensaje, tipo):
        if tipo == "success":
            st.success(mensaje)
        elif tipo == "error":
            st.error(mensaje)

    def mostrar_usuarios(self, usuarios, controlador):
        st.subheader("Usuarios Registrados")
        st.dataframe(usuarios)
