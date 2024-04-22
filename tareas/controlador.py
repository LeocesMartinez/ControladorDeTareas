from flask import Flask, request, abort
import traceback
from flask_cors import CORS

#from manejadorTareas import crearTarea
from serivicios.manejadorUsuario import ManejadorUsuario, ERROR_CONSULTAR_USUARIO, ERROR_REGISTRAR_USUARIO, ERROR_LOGIN_USUARIO
from serivicios.manejadorTareas import ManejadorTarea, ERROR_CREAR_TAREA
import datetime
#from conexion import Conexion
#Conexion.conectar()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

#Consultas GET para devolver una lista de registros
@app.route('/consultar-usuarios')
def consultar_usuarios():
    try:
        manejadorUsuario = ManejadorUsuario()
        return manejadorUsuario.consultar()
    except Exception as e:
        traceback.print_exc()
        abort(500, ERROR_LOGIN_USUARIO +  str(e))        


@app.route('/registrar-usuario', methods=['POST'])
def registro():
    try:
        username = request.form.get('usuarioId')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        password = request.form.get('password')     
        
        manejadorUsuario = ManejadorUsuario()
        return manejadorUsuario.registrar(username, nombre, apellido, password)
    except Exception as e:
        traceback.print_exc()
        abort(500, ERROR_REGISTRAR_USUARIO + str(e))  

@app.route('/login-usuario', methods=['POST'])
def login_usuario():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        
        manejadorUsuario = ManejadorUsuario()
        return manejadorUsuario.login(username, password)
    except Exception as e:
        traceback.print_exc()
        abort(500, ERROR_CONSULTAR_USUARIO + str(e))         

  
@app.route('/crearTareas', methods=["POST"])
def crear_tarea():
    try:
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')        
        fechaVencimiento = request.form.get('fechaVencimiento')
        prioridad = request.form.get('prioridad')    
        usuario_creador = request.form.get('creadorTarea')

        manejadorTareas = ManejadorTarea()
        return manejadorTareas.crearTarea(titulo, descripcion,fechaVencimiento,prioridad,usuario_creador)    
    except Exception as e:
        traceback.print_exc()
        abort(500, ERROR_CREAR_TAREA + str(e))

#@app.route('/marcarTareaCompletada', methods=["PUT"])
#def marcar_tarea_completada():



#@app.route('/verHistorial')


url = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
    #webbrowser.open(url)ls    
    app.run(debug=True)