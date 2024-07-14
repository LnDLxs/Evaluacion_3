from flask import Flask 
from flask import render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods= ['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        Nota1 = int(request.form['Nota1'])
        Nota2 = int(request.form['Nota2'])
        Nota3 = int(request.form['Nota3'])
        Asistencia = int(request.form['asistencia'])

        promedio = (Nota1 + Nota2 + Nota3) / 3 
        if promedio >= 40 and Asistencia >= 75:
            estado = 'Aprobado'
        else:
            estado = 'Reprobado'
        return render_template(template_name_or_list='ejercicio1.html', resu= estado,prome = promedio) 
    return render_template(template_name_or_list='ejercicio1.html', resu= "") 

@app.route('/ejercicio2', methods = ['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        return render_template('ejercicio2.html',nombre_mas_largo=nombre_mas_largo,longitud=len(nombre_mas_largo))
    else:
            error_message = "Por favor, complete todos los campos."
            return render_template('ejercicio2.html', error_message=error_message)
    return render_template('ejercicio2.html')   

if __name__ == '__main__':
    app.run(debug=True,port=5000)