import pyodbc

class Conexion:
    def __init__(self):
        pass
    
    def __conectar(self):
        SERVER = 'PMVM460\SQL2019'
        DATABASE = 'MiBaseDeDatos'
        USERNAME = 'LeoGlobal'
        PASSWORD = 'Yeilis1063.,'
        connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes'
        #conn = pyodbc.connect(connectionString)
        #cursor = conn.cursor()

        #try:
        conn = pyodbc.connect(connectionString)
        print('Conexión exitosa')
        #return cursor
        return conn
        #except pyodbc.Error as e:
        #    print(f'Error al conectar a la base de datos: {e}')
        # conn.close
    
    def ejecutar_consulta(self, consulta, parametros):
        conn = self.__conectar()
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        resultado = cursor.fetchall()
        conn.close
        return resultado
    
    def ejecutar_consulta_unica(self, consulta, parametros):
        conn = self.__conectar()
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        resultado = cursor.fetchone() #como se espera un unico resultado se cambia el metodo
        conn.close
        return resultado
    
    def ejecutar_insertar(self, consulta, parametros):
        conn = self.__conectar()
        cursor = conn.cursor()
        print(consulta,'aqui ver', parametros)
        cursor.execute(consulta, parametros)
        conn.commit()
        cursor.execute("SELECT @@IDENTITY")
        row = cursor.fetchone()
        print (row, 'rows')
        last_id = row[0] if row is not None else None
        cursor.close()
        conn.close()
        return last_id
    
    def ejecutar_actualizar(self, consulta, parametros):
        conn = self.__conectar()
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        conn.commit()
        cursor.close()
        conn.close()
        
    def ejecutar_eliminar(self, consulta, parametros):
        conn = self.__conectar()
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        conn.commit()
        cursor.close()
        conn.close()