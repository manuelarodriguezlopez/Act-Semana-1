from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

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