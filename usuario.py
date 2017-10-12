class Usuario:
    def __init__(self):
        self.usuarios = []
        self.usuario_borrado = " "
        usuario={'usuario' : "Pepe" , 'contrasenha' : "1234" }
        self.usuarios.append(usuario)

    def anhadir_usuario(self, nombre, contrasenha):
        nombres=nombre
        contrasena=contrasenha
        usuario={'usuario' : nombre , 'contrasenha' : contrasenha }
        self.usuarios.append(usuario)
    def borrar_usuario(self, nombre, contrasenha):
        nombres=nombre
        contrasena=contrasenha
        usuario_borrado=nombre
        self.usuarios.remove({'usuario' : nombre , 'contrasenha' : contrasena })
    def getUsuarios(self):
        return self.usuarios
    def getUltimoUsuarioBorrado(self):
        return self.usuario_borrado
