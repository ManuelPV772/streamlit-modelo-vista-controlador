class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        # Mostrar título
        self.vista.mostrar_titulo()

        # Manejo del formulario
        name, age, guardar_presionado = self.vista.mostrar_formulario()

        if guardar_presionado:
            if name and age:
                # Lógica de guardar usuario
                self.modelo.insertar_usuario(name, age)
                self.vista.mostrar_mensaje(f"Usuario {name} agregado correctamente.", "success")
            else:
                self.vista.mostrar_mensaje("Por favor, completa todos los campos.", "error")

        # Mostrar usuarios registrados
        usuarios = self.modelo.obtener_usuarios()
        self.vista.mostrar_usuarios(usuarios, self)
