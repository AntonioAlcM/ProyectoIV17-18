# -*- coding: utf-8 -*-
import unittest

from usuario import Usuario

class SoloTest(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario()
    def test_usuarios_es_una_lista(self):
        self.assertNotIsInstance( self.usuario.getUsuarios, list , "El objeto usuario no es una lista")
    def test_anhadir_usuario(self):
        este_usuario=self.usuario.getUsuarios()
        ultima_entrada=len(este_usuario)-1
        self.assertTrue(este_usuario[ultima_entrada]['usuario'].isalpha(), "El usuario contiene números")
        self.assertTrue(este_usuario[ultima_entrada]['contrasenha'].isalnum(), "La contraseña no contiene números")
    def test_borrado_ultimo_usuario(self):
        este_usuario=self.usuario.getUsuarios()
        ultimo_usuario_borrado=self.usuario.getUltimoUsuarioBorrado()
        for i in range(0,len(este_usuario)):
            self.assertNotEqual(este_usuario[i]['usuario'],ultimo_usuario_borrado, "El usuario no se ha borrado")




if __name__ == '__main__':
    unittest.main()
