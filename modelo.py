class Modelo:
    def __init__(self, conn):
        self.conn = conn

    def obtener_usuarios(self):
        return self.conn.query("SELECT id, name, age FROM users")

    def insertar_usuario(self, name, age):
        with self.conn.session as s:
            s.execute(
                "INSERT INTO users (name, age) VALUES (:name, :age);",
                params=dict(name=name, age=age),
            )
            s.commit()

    def actualizar_usuario(self, user_id, new_name, new_age):
        with self.conn.session as s:
            s.execute(
                "UPDATE users SET name = :name, age = :age WHERE id = :id;",
                params=dict(name=new_name, age=new_age, id=user_id),
            )
            s.commit()

    def eliminar_usuario(self, user_id):
        with self.conn.session as s:
            s.execute("DELETE FROM users WHERE id = :id;", params=dict(id=user_id))
            s.commit()
