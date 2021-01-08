import numpy as np
from flask import Flask, request,render_template,jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    android_developer = 0 
    laravel_developer = 0 
    web_developer = 0
    react_native_developer=0
    flutter_developer=0
    nodejs_developer=0
    database_administrator=0
    php_developer=0
    net_developer=0
    kotlin_developer=0
    full_stack_developer=0
    digital_marketing=0
    network_administrator=0
    experience = 0
    if (request.form['job'] == "Laravel Developer"):
        laravel_developer = 1
    if (request.form['job'] == "Android Developer"):
        android_developer = 1
    if (request.form['job'] == "Web Developer"):
        web_developer = 1
    if (request.form['job'] == "React native developer"):
        react_native_developer = 1
    if (request.form['job'] == "Flutter developer"):
        flutter_developer = 1
    if (request.form['job'] == "Nodejs developer"):
        nodejs_developer = 1
    if (request.form['job'] == "Database administrator"):
        database_administrator = 1
    if (request.form['job'] == "Php developer"):
        php_developer = 1
    if (request.form['job'] == ".NET Developer"):
        net_developer = 1
    if (request.form['job'] == "Kotlin Developer"):
        kotlin_developer = 1
    if (request.form['job'] == "Full Stack Developerr"):
        full_stack_developer = 1
    if (request.form['job'] == "Digital Marketing"):
        digital_marketing = 1
    if (request.form['job'] == "Network Administrator"):
        network_administrator = 1
    else:
        laravel_developer = 0
    experience = float(request.form['experience'])
   
    prediction = model.predict([[android_developer,laravel_developer,web_developer,react_native_developer,
    flutter_developer,nodejs_developer,database_administrator,php_developer,net_developer,
    kotlin_developer,full_stack_developer,digital_marketing,network_administrator,experience]])
    output = round(prediction[0], 2)
    return jsonify({'salar_prediction': str(output)}), 201
    '''
    

    Returns
    -------
    None.

    '''
if __name__ == "__main__":
    app.run(debug=True)