from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

data = {
    "Distancia Recorrida": [2],
    "Pasajeros": [1],
    "Precio": [5500]
}

df = pd.DataFrame(data)
x = df[["Distancia Recorrida","Pasajeros"]]
y = df["Precio"]
model = LinearRegression()
model.fit(x, y)
def CalculateGrade(distancia,pasajeros):
    result = model.predict([[distancia,pasajeros]])[0]
    return round(result)