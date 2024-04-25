from flask import Flask, request, abort
import traceback
from flask_cors import CORS
from serivicios.manejadorUsuario import ManejadorUsuario, ERROR_CONSULTAR_USUARIO, ERROR_REGISTRAR_USUARIO, ERROR_LOGIN_USUARIO
from serivicios.manejadorTareas import ManejadorTarea, ERROR_CREAR_TAREA, ERROR_MOSTRAR_TAREA, QUERY_ELIMINAR_HISTORIAL_TAREA, ERROR_REASIGNAR_TAREA, ERROR_ELIMINAR_TAREA, ERROR_COMPLETAR_TAREA
import datetime


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
        abort(500, ERROR_CONSULTAR_USUARIO +  str(e))        


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
        abort(500, ERROR_LOGIN_USUARIO + str(e))         

  
@app.route('/crear-tareas', methods=["POST"])
def crear_tarea():
    try:
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')        
        fechaVencimiento = request.form.get('fechaVencimiento')
        prioridad = request.form.get('prioridad')    
        usuario_creador = request.form.get('creadorTarea')
        usuario_asignado = request.form.get('usuario_asignado')

        manejadorTareas = ManejadorTarea()
        return manejadorTareas.crearTarea(titulo, descripcion, fechaVencimiento, prioridad, usuario_creador, usuario_asignado)    
    except Exception as e:
        traceback.print_exc()
        abort(500, ERROR_CREAR_TAREA + str(e))
        
@app.route('/mostrar-tareas', methods=["GET"])
def mostrar_tarea():
    try:
        usuario_asignado = request.args.get('usuarioAsignado')
        estado = request.args.get('estado')
        print('parametros', usuario_asignado, estado)
        manejadorTareas = ManejadorTarea()
        return manejadorTareas.mostrarTarea(usuario_asignado, estado)
        
    except Exception as e:
        traceback.print_exc()
        abort(500, ERROR_MOSTRAR_TAREA + str(e))
        
@app.route('/reasignar-tarea', methods=["PUT"])
def reasignar_tarea():
    try:
        tareaId = request.form.get('tareaId')
        usuarioAsignador = request.form.get('usuarioAsignador')
        usuarioAsignado = request.form.get('usuarioAsignado')
        
        manejadorTareas = ManejadorTarea()
        return manejadorTareas.reasignarTarea(tareaId, usuarioAsignador, usuarioAsignado)
        
    except Exception as e:
        traceback.print_exc()
        abort(500, ERROR_REASIGNAR_TAREA+ str(e))

@app.route('/eliminar-tarea', methods=["DELETE"])
def eliminar_tarea():
    try:
        tareaId = request.form.get('tareaId')

        manejadorTareas = ManejadorTarea()
        return manejadorTareas.eliminarTarea(tareaId)
    
    except Exception as e:
        traceback.print_exc()
        # corregir
        abort(500, ERROR_ELIMINAR_TAREA + str(e))

   
@app.route('/marcarTareaCompletada', methods=["PUT"])
def marcar_tarea_completada():
    try:
        tareaId = request.form.get('tareaId')
        usuarioModificador = request.form.get('usuarioModificador')
        
        
        manejadorTareas = ManejadorTarea()
        return manejadorTareas.marcarComoCompletada(tareaId, usuarioModificador)    
    except Exception as e:
        traceback.print_exc()
        abort(500, ERROR_COMPLETAR_TAREA  + str(e))
        
# opcional cambiarle la fecha de vencimiento a una tarea y cambiar la prioridad
# importar los errores y cuadrarlos en los métodos

url = 'http://127.0.0.1:5000/'

if __name__ == "__main__":
    #webbrowser.open(url)ls    
    app.run(debug=True)