import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report



def entrenar_modelo(csv_file='adolescentes_sobrepeso.csv'):
    # Cargar datos
    data = pd.read_csv(csv_file)
    print(data.head())
    print(data.info())
    print(data.describe())
    
    # Separar features y target
    X = data.drop('Sobrepeso', axis=1)
    y = data['Sobrepeso']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Escalado
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Modelo de regresión logística
    Logistic_model = LogisticRegression()
    Logistic_model.fit(X_train_scaled, y_train)
    
    return Logistic_model, scaler, X_test_scaled, y_test


def evaluar_modelo(model, X_test, y_test, filename=None):
    # Si no se pasa filename, generar uno único
    if filename is None:
        filename = f"static/images/confusion_matrix_{int(time.time())}.png"

    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    accuracy = accuracy_score(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 5))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.xlabel('Predicho')
    plt.ylabel('Real')
    plt.title('Matriz de Confusión')
    plt.savefig(filename)
    plt.close()

    return {"accuracy": accuracy, "report": report, "matrix": matrix, "image": filename}

def Predecir(model, scaler, features):
    X = np.array(features).reshape(1, -1)
    X_scaled = scaler.transform(X)
    prob = model.predict_proba(X_scaled)[0][1]
    result = "Sí" if prob >= 0.5 else "No"
    return result, round(prob, 4)