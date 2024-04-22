from flask import jsonify
from conexion import Conexion

QUERY_REGISTAR = "INSERT INTO Tareas (titulo, descripcion,fecha_vencimiento,prioridad,usuario_creador) VALUES (?,?,?,?,?)"
QUERY_HISTORICO = "INSERT INTO HistoricoTareas (evento, tarea, usuario)VALUES (?,?,?)"
ERROR_CREAR_TAREA = "ERROR al crear la tarea"

class ManejadorTarea:
    
    def __init__(self):
        self.__conexion = Conexion()

    def crearTarea(self, titulo, descripcion,fechaVencimiento,prioridad,usuario_creador):        
        parametros = (titulo, descripcion,fechaVencimiento,prioridad,usuario_creador)
        resultado = self.__conexion.ejecutar_insertar(QUERY_REGISTAR, parametros)

        evento = 'CREACION'
        parametrosHistorico = (evento, resultado, usuario_creador)
        resultado = self.__conexion.ejecutar_insertar(QUERY_HISTORICO, parametrosHistorico)
        #if resultado == 'OK':
        return jsonify({'resultado': 'tarea creada con éxito'})
        #return "Tarea"


    
    def verHistorial():
        return "historial"