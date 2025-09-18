import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score, classification_report

data=pd.read_csv('adolescentes_sobrepeso.csv')

print(data.head())
print(data.info())
print(data.describe())

x=data.drop('Sobrepeso',axis=1)
y=data['Sobrepeso']

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.5, random_state=42)
scarler=StandardScaler()
x_train_scaled=scarler.fit_transform(x_train)
x_test_scaled=scarler.transform(x_test)
#modulo de regresion logistica
Logistic_model=LogisticRegression()
#entrenamiento del modelo
Logistic_model.fit(x_train_scaled,y_train)

#predicciones con el conjunto de prueba 
y_pred=Logistic_model.predict(x_test_scaled)

#crear la matriz de confucion
conf_matrix=confusion_matrix(y_test,y_pred)
plt.figure(figsize=(8,6))
sns.heatmap(conf_matrix,annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicho')
plt.ylabel('Real')
plt.title('Confusion Matrix')
plt.savefig("static/confusion_matrix.png")



#imprimir el reporte de clasificacion
print(classification_report(y_test, y_pred))

#imprimir la exactirud del modelo 
accuracy= accuracy_score(y_test,y_pred)
print(f'Exactitud del modelo: {accuracy * 100:.2f}%')#2f sirve como aproximacion dos cifras despues del punto
