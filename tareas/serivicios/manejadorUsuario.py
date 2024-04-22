from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from conexion import Conexion

QUERY_CONSULTAR = "SELECT * FROM Usuario"
QUERY_CONSULTAR_UNICA = "SELECT * FROM Usuario WHERE usuarioId = ?"
QUERY_REGISTAR = "INSERT INTO Usuario (usuarioId, nombre, apellido, contrasenia) VALUES (?, ?, ?,?)"

ERROR_CONSULTAR_USUARIO = "Ha ocurrido un error consultando usuarios: "
ERROR_LOGIN_USUARIO = "Ha ocurrido un error en el login del usuario: "
ERROR_REGISTRAR_USUARIO = "Ha ocurrido un error resgistrando usuario "

class ManejadorUsuario:
    def __init__(self):
        self.__conexion = Conexion()
        
    def consultar(self):
        resultado = self.__conexion.ejecutar_consulta(QUERY_CONSULTAR, ())
        
        usuarios = []
        for row in resultado:
            usuario = {'UsuarioId': row[0], 'nombre': row[1], 'apellido': row[2]}
            usuarios.append(usuario)
        
        return jsonify(usuarios)
    

    def registrar(self,username, nombre, apellido, password):
        hashed_password = generate_password_hash(password)
        parametros = (username, nombre, apellido, hashed_password)
        resultado = self.__conexion.ejecutar_insertar(QUERY_REGISTAR, parametros)
        #if resultado == 0:
        return jsonify({'resultado': 'usuario registrado exitosamente'})
        
    
    def login(self, usuario, password):
        parametros = (usuario) #Se pasa el usuario como parametro de consulta para filtrar datos de la BD
        resultado = self.__conexion.ejecutar_consulta_unica(QUERY_CONSULTAR_UNICA, parametros)
        
        
        if (resultado):
            print("resultado", resultado)    
            if(check_password_hash(resultado[3], password)):  
                return jsonify({"resultado": "login_exitoso, Bienvenid@"})
            else:
                raise Exception('Usuario no existe y/o contraseña incorrectas.')               
        else:
            raise Exception('Usuario no existe y/o contraseña incorrectas')