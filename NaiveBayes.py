import pandas as pd
import numpy as np
import time, io, os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

def entrenar_modelo(csv_file='NaiveBayes.csv', random_state=42):
    data = pd.read_csv(csv_file)
    X = data[['mensaje','prioridad','palabras_clave','hora']].copy()
    y = data['categoria']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=random_state)
    
    def concat_text(df):
        return (df['mensaje'].fillna('') + ' ' + df['palabras_clave'].fillna('')).values
    
    text_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=2000))
    ])
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])


    X_train_text = concat_text(X_train)
    X_test_text = concat_text(X_test)
    text_vec = TfidfVectorizer(ngram_range=(1,2), max_features=2000)
    X_train_text_vec = text_vec.fit_transform(X_train_text)
    X_test_text_vec = text_vec.transform(X_test_text)

    
    cat_enc = OneHotEncoder(handle_unknown='ignore', sparse=False)
    X_train_cat = cat_enc.fit_transform(X_train[['prioridad']])
    X_test_cat = cat_enc.transform(X_test[['prioridad']])

    
    scaler = StandardScaler()
    X_train_num = scaler.fit_transform(X_train[['hora']])
    X_test_num = scaler.transform(X_test[['hora']])

    
    from scipy.sparse import hstack, csr_matrix
    X_train_comb = hstack([X_train_text_vec, csr_matrix(X_train_cat), csr_matrix(X_train_num)])
    X_test_comb = hstack([X_test_text_vec, csr_matrix(X_test_cat), csr_matrix(X_test_num)])

    
    model = ComplementNB()  
    model.fit(X_train_comb, y_train)

 
    artifacts = {
        'model': model,
        'text_vec': text_vec,
        'cat_enc': cat_enc,
        'scaler': scaler,
        'X_test_comb': X_test_comb,
        'y_test': y_test,
        'X_test': X_test,  
    }
    return artifacts

def evaluar_modelo(artifacts, imagen_path=None):
    model = artifacts['model']
    X_test = artifacts['X_test_comb']
    y_test = artifacts['y_test']

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    matrix = confusion_matrix(y_test, y_pred, labels=model.classes_)

    if imagen_path is None:
        imagen_path = f"static/images/confusion_nb_{int(time.time())}.png"
    os.makedirs(os.path.dirname(imagen_path), exist_ok=True)
    plt.figure(figsize=(5,4))
    sns.heatmap(matrix, annot=True, fmt='d', cbar=False)
    plt.ylabel('Real')
    plt.xlabel('Predicho')
    plt.title('Matriz de Confusión - Naive Bayes')
    plt.xticks(ticks=np.arange(len(model.classes_))+0.5, labels=model.classes_)
    plt.yticks(ticks=np.arange(len(model.classes_))+0.5, labels=model.classes_)
    plt.tight_layout()
    plt.savefig(imagen_path)
    plt.close()

    return {"accuracy": round(acc,4), "report": report, "matrix": matrix, "image": imagen_path, "classes": list(model.classes_)}

def predict_label(artifacts, mensaje, prioridad, palabras_clave, hora, threshold=None):
    text_input = (mensaje or '') + ' ' + (palabras_clave or '')
    text_vec = artifacts['text_vec'].transform([text_input])
    cat = artifacts['cat_enc'].transform([[prioridad]])  
    num = artifacts['scaler'].transform([[float(hora)]])
    from scipy.sparse import hstack, csr_matrix
    X_comb = hstack([text_vec, csr_matrix(cat), csr_matrix(num)])
    probs = artifacts['model'].predict_proba(X_comb)[0]
    classes = list(artifacts['model'].classes_)
    idx = probs.argmax()
    pred = classes[idx]
    prob = float(probs[idx])
    if threshold is not None:
        try:
            th = float(threshold)
            if prob < th:
                return {"prediction": "Indeterminado", "probability": round(prob,4), "class_probs": dict(zip(classes, [round(float(p),4) for p in probs]))}
        except:
            pass
    return {"prediction": pred, "probability": round(prob,4), "class_probs": dict(zip(classes, [round(float(p),4) for p in probs]))}

if __name__ == '__main__':
    artifacts = entrenar_modelo(csv_file='tickets_naivebayes.csv')
    metrics = evaluar_modelo(artifacts)
    print('Accuracy:', metrics['accuracy'])
    print('Classes:', metrics['classes'])

    example = predict_label(artifacts, "No puedo conectarme al wifi en mi oficina", "Alta", "wifi,red", 9)
    print('Ejemplo predict:', example)

