from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="ACL2005",  
        database="sie_alumnos"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    conn.close()
    return render_template('index.html', alumnos=alumnos)

@app.route('/add', methods=['POST'])
def add_alumno():
    matricula = request.form['matricula']
    nombre = request.form['nombre']
    edad = request.form['edad']
    semestre = request.form['semestre']
    carrera = request.form['carrera']
    calificacion = request.form['calificacion']
    estatus = request.form['estatus']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alumnos (Matricula, Nombre_Completo, Edad, Semestre, Carrera, Calificacion_final, Estatus) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (matricula, nombre, edad, semestre, carrera, calificacion, estatus))
    conn.commit()
    conn.close()
    
    return redirect('/')

@app.route('/delete/<int:matricula>')
def delete_alumno(matricula):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alumnos WHERE Matricula = %s", (matricula,))
    conn.commit()
    conn.close()
    
    return redirect('/')

@app.route('/update', methods=['POST'])
def update_alumno():
    matricula = request.form['matricula']
    nombre = request.form['nombre']
    edad = request.form['edad']
    semestre = request.form['semestre']
    carrera = request.form['carrera']
    calificacion = request.form['calificacion']
    estatus = request.form['estatus']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE alumnos SET Nombre_Completo=%s, Edad=%s, Semestre=%s, Carrera=%s, Calificacion_final=%s, Estatus=%s WHERE Matricula=%s",
                   (nombre, edad, semestre, carrera, calificacion, estatus, matricula))
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
