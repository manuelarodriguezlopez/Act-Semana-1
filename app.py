from flask import Flask, render_template, request, url_for
###########################################3
##agregé estas dos para que funcione la actualizacion de los datos
import matplotlib
matplotlib.use('Agg')
##########################################
import matplotlib.pyplot as plt
import numpy as np
import os
import LRModel
from LRModel import CalculateGrade
import LogRep

app = Flask(__name__)


@app.route('/')
def index():
    Username = "Mateo"
    return render_template('index2.html', name=Username)


@app.route('/casoUno')
def casoUno():
    Username = "Mateo"
    return render_template('casoUno.html', name=Username)

@app.route('/casoDos')
def casoDos():
    Username = "Mateo"
    return render_template('casodos.html', name=Username)

@app.route('/casoTres')
def casoTres():
    Username = "Mateo"
    return render_template('casoTres.html', name=Username)

@app.route('/casoCuatro')
def casoCuatro():
    Username = "Mateo"
    return render_template('casoCuatro.html', name=Username)

@app.route('/regresionConceptos')
def regresionConceptos():
    return render_template("rlconceptos.html")


@app.route('/LR', methods=["GET", "POST"])
def LR():
    df = LRModel.df  
    media = df["Precio"].mean()
    mediana = df["Precio"].median()
##estos son variables para guardar resultados, se inician en cero
    calculateResult = None
    distancia = None
    pasajeros = None
    message = None 
##si los datos vienen con precio eso quiere decir que es actualizar. (UpdateData)
##si no viene con precio quiere decir que es calcular (calculateGrade)
    if request.method == "POST":
        if "precio" in request.form:
            distancia = float(request.form["distancia"])
            pasajeros = float(request.form["pasajeros"])
            precio = float(request.form["precio"])
            message = LRModel.UpdateData(distancia, pasajeros, precio)
        else:
            distancia = float(request.form["distancia"])
            pasajeros = float(request.form["pasajeros"])
            calculateResult = CalculateGrade(distancia, pasajeros)

    image_path = os.path.join('static', 'images')
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    plt.figure(figsize=(8, 6))
    plt.scatter(df["Distancia Recorrida"], df["Precio"], color='blue', s=80, label='Datos')
    x_vals = np.linspace(df["Distancia Recorrida"].min(), df["Distancia Recorrida"].max(), 100)
    y_vals = [CalculateGrade(x, 1) for x in x_vals]  
    plt.plot(x_vals, y_vals, color='orange', linewidth=2, label='Línea de Regresión')

    plt.title('Gráfico de Dispersión y Linea de Regresión')
    plt.xlabel('Distancia Recorrida')
    plt.ylabel('Precio')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    graph_file = os.path.join(image_path, 'grafico.png')
    plt.savefig(graph_file)
    plt.close()

    return render_template(
        "rl.html",
        result=calculateResult,
        graph_url=url_for('static', filename='images/grafico.png'),
        media=media,
        mediana=mediana,
        message=message  
    )
@app.route('/LogisConceptos')
def LogisConceptos():
    return render_template("logisconceptos.html")
@app.route('/Lc')
def Lc():
    return render_template("Lc.html")