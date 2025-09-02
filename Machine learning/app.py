from flask import Flask
from flask import render_template

app= Flask(__name__)

@app.route('/')
def home():
    a = None
    a = "Flask"
    return "Hello, "+a+"!"

if __name__ =='__main__':
    app.run(debug=True)

@app.route('/index')
def index():
    Username = " Mateo"
    return render_template('index2.html',name=Username)

