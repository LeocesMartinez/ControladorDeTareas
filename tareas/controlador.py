from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import webbrowser
import jwt
import pyodbc


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
 
# Lista en memoria para almacenar los usuarios registrados (simulación de base de datos)
# Hacerlo por conexión a bases de datos

usuarios = {}


@app.route('/')
def index():
    # Obtener el mensaje de la sesión iniciada correctamente (si existe)
    message = request.args.get('message')
    return render_template('interfaz.html', message=message)

# Ruta para la página de usuario
@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        return render_template('index.html', message="Interfaz de Usuario")  

@app.route('/registrarse', methods=['POST'])
def registrarse():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
       # role = request.form.get('role','user')  # Definir el rol por defecto como 'user'
        
        
        # Verificar si el usuario ya está registrado
        if username in usuarios:
            return render_template('index.html', message='El usuario ya está registrado')

        # Hash de la contraseña antes de almacenarla
        hashed_password = generate_password_hash(password)

        # Agregar el nuevo usuario al diccionario de usuarios con la contraseña hasheada y el rol
        usuarios[username] = {'password': hashed_password}

        print("Usuario registrado con éxito:", username)
        print('registro en usuario')
       # print(role)

        # Redireccionar a la página de inicio con un mensaje de registro exitoso
       # return redirect(url_for('index', message='Registro exitoso, inicia sesión con tu usuario'))
        return render_template('index.html', message='Registro exitoso, inicia sesión con tu usuario')
    except Exception as e:
        return render_template('error.html', message=str(e))

@app.route('/loginUser', methods=['POST'])
# IMPLEMENTAR EL JWT


def loginUser():
    try:
        username = request.form.get('username')
        password = request.form.get('password')      
        
        # Verificar si el usuario está registrado
        if username in usuarios:
            # Verificar si la contraseña coincide
            if check_password_hash(usuarios[username]['password'], password):
    
              #  if usuarios[username]:                
                    return redirect(url_for('menu', message='Sesión iniciada correctamente'))
                #else:            
                 #   return render_template('error.html', message='No tienes permiso para acceder como administrador')
                                   
            else:
                return render_template('index.html', message='Usuario o contraseña incorrectos')
        else:
            return render_template('index.html', message='Usuario no registrado')
    except Exception as e:
        return render_template('error.html', message=str(e))

@app.route('/menu')
def menu():
    message = request.args.get('message')
    return render_template('menu.html', message=message)


url = 'http://127.0.0.1:5000/'
if __name__ == "__main__":
    webbrowser.open(url)
    app.run(debug=True)
