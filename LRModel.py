from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
##################no encontre la forma de hacer que los datos se agregen en estos espacios directamente#######
###########asi que la básicamente los datos son los mismos siempre cuando se inicia el debug############
############sinembargo por lo visto la tabla si actualiza los datos cuando mantenemos el debug#########3
data = {
    "Distancia Recorrida": [2, 5, 7, 10, 3, 8, 12, 15, 6, 20, 18, 25, 30, 22, 28],
    "Pasajeros": [1, 2, 3, 1, 4, 2, 5, 3, 2, 6, 4, 5, 7, 3, 6],
    "Precio": [5500, 13000, 18000, 20500, 9500, 18500, 28500, 34500, 14500, 47000, 39500, 53500, 67500, 45500, 63500]
}
df = pd.DataFrame(data)
x = df[["Distancia Recorrida","Pasajeros"]]
y = df["Precio"]
model = LinearRegression()
model.fit(x, y)
def CalculateGrade(distancia,pasajeros):
    result = model.predict([[distancia,pasajeros]])[0]
    return round(result)
##esto es para actualizar el modelo de datos##
def UpdateData(distancia, pasajeros, precio):
    global df, model
    new_row = pd.DataFrame({
        "Distancia Recorrida": [distancia],
        "Pasajeros": [pasajeros],
        "Precio": [precio]
    })

    df = pd.concat([df, new_row], ignore_index=True)
    x = df[["Distancia Recorrida", "Pasajeros"]]
    y = df["Precio"]
    model = LinearRegression()
    model.fit(x, y)
    return "Datos actualizados"