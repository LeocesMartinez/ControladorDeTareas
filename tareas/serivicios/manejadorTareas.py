from flask import jsonify
from conexion import Conexion

QUERY_CREAR_TAREA = "INSERT INTO Tareas (titulo, descripcion,fecha_vencimiento,prioridad,usuario_creador,usuario_asignado) VALUES (?,?,?,?,?,?)"
QUERY_HISTORICO = "INSERT INTO HistoricoTareas (evento, tarea, usuario)VALUES (?,?,?)"
QUERY_MOSTRAR_TAREA = "SELECT  * from Tareas where usuario_asignado = ? and estado = ?"
QUERY_REASIGNAR_TAREA = "UPDATE Tareas SET usuario_asignado = ? WHERE tareaId = ?"

ERROR_CREAR_TAREA = "ERROR al crear la tarea"
ERROR_MOSTRAR_TAREA = "ERROR al mostrar la tarea"

class ManejadorTarea:
    
    def __init__(self):
        self.__conexion = Conexion()

    def crearTarea(self, titulo, descripcion,fechaVencimiento,prioridad,usuario_creador,usuario_asignado):        
        parametros = (titulo, descripcion,fechaVencimiento,prioridad,usuario_creador,usuario_asignado)
        resultado = self.__conexion.ejecutar_insertar(QUERY_CREAR_TAREA, parametros)

        evento = 'CREACION'
        parametrosHistorico = (evento, resultado, usuario_creador)
        resultado = self.__conexion.ejecutar_insertar(QUERY_HISTORICO, parametrosHistorico)
        #if resultado == 'OK':
        return jsonify({'resultado': 'tarea creada con éxito'})
        #return "Tarea"
        
    def mostrarTarea(self, usuario_asignado, estado):
        parametrosMostrarTarea = (usuario_asignado, estado)
        resultado = self.__conexion.ejecutar_consulta(QUERY_MOSTRAR_TAREA, parametrosMostrarTarea)
        tareas = []
        for row in resultado:
            tarea = {'tareaId': row[0], 'titulo': row[1], 'descripcion': row[2], 'fecha_creacion': row[3], 
                     'fecha_vencimiento': row[4], 'prioridad': row[5], 'estado': row[6], 'usuario_creador': row[7],
                     'usuario_asignado':row[8]}
            tareas.append(tarea)
        
        return jsonify(tareas)

    def reasignarTarea(self, tareaId, usuarioAsignador, usuarioAsginado):
        parametrosReasignar = (usuarioAsginado, tareaId)
        self.__conexion.ejecutar_actualizar(QUERY_REASIGNAR_TAREA, parametrosReasignar)
        
        evento = 'MODIFICACION'
        parametrosHistorico = (evento, tareaId, usuarioAsignador)
        resultado = self.__conexion.ejecutar_insertar(QUERY_HISTORICO, parametrosHistorico)
        
        return jsonify({'resultado':'tarea asignada con éxito'})
    def marcarComoCompleta(self):
        # Cambiar el estado a completado, guardar como completado 
        
        return ''
    
    def consultarHistorico(self):
        #hacer un get para que arroje la lista de tareas ordenadas y filtradas
        return ''
        
    def verHistorial():
        return "historial"