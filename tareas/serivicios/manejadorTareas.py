from flask import jsonify
from conexion import Conexion

QUERY_CREAR_TAREA = "INSERT INTO Tareas (titulo, descripcion,fecha_vencimiento,prioridad,usuario_creador,usuario_asignado) VALUES (?,?,?,?,?,?)"
QUERY_HISTORICO = "INSERT INTO HistoricoTareas (evento, tarea, usuario)VALUES (?,?,?)"

QUERY_MOSTRAR_TAREA = "SELECT  * from Tareas where usuario_asignado = ? and estado = ?"
QUERY_REASIGNAR_TAREA = "UPDATE Tareas SET usuario_asignado = ? WHERE tareaId = ?"
QUERY_MARCAR_COMO_COMPLETADA = "UPDATE Tareas SET estado = ? WHERE tareaId = ?"
QUERY_ELIMINAR_HISTORIAL_TAREA = "DELETE FROM HistoricoTareas WHERE tarea = ?"
QUERY_ELIMINAR_TAREA = "DELETE FROM Tareas WHERE tareaId = ?"


ERROR_CREAR_TAREA = "ERROR al crear la tarea"
ERROR_MOSTRAR_TAREA = "ERROR al mostrar la tarea"
ERROR_REASIGNAR_TAREA = "ERRROR al reasignar tarea"
ERROR_COMPLETAR_TAREA = "ERROR al completar tarea"
ERROR_ELIMINAR_TAREA = "ERROR al eliminar tarea"

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
    
    # Revisar hacia abajo
    def eliminarTarea(self, tareaId):
        parametrosEliminarHistorial = (tareaId)
        self.__conexion.ejecutar_eliminar(QUERY_ELIMINAR_HISTORIAL_TAREA, parametrosEliminarHistorial)    
        
        parametrosEliminar = (tareaId)
        self.__conexion.ejecutar_eliminar(QUERY_ELIMINAR_TAREA, parametrosEliminar)    
        
        return jsonify({'resultado': 'Tarea eliminada con éxito'})
    
    def marcarComoCompletada(self, tareaId, usuarioModificador):
        estado = 'COMPLETADA'
        parametrosMarcarComoCompletada = (estado, tareaId)#, estado, usuarioModificador)
        self.__conexion.ejecutar_actualizar(QUERY_MARCAR_COMO_COMPLETADA, parametrosMarcarComoCompletada)
        
        evento = 'COMPLETADA'        
        parametrosHistorico = (evento, tareaId, usuarioModificador )#, usuarioModificador)
        resultado = self.__conexion.ejecutar_insertar(QUERY_HISTORICO, parametrosHistorico)
        
        # Cambiar el estado a completado, guardar como completado         
        return jsonify({'resultado': 'tarea completada con éxito'})

    def listaDePendientes(self):
        return ' '


    def consultarHistorico(self):
        #hacer un get para que arroje la lista de tareas ordenadas y filtradas
        return ''
        
    def verHistorial():
        return "historial"