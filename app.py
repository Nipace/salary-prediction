import numpy as np
from flask import Flask, request,render_template
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
    experience = 0
    if (request.form['job'] == "Laravel Developer"):
        laravel_developer = 1
    if (request.form['job'] == "Android Developer"):
        android_developer = 1
    if (request.form['job'] == "Web Developer"):
        web_developer = 1
    else:
        laravel_developer = 0
    experience = float(request.form['experience'])
   
    prediction = model.predict([[android_developer,laravel_developer,web_developer,experience]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text = "Salary Prediction is Rs {}".format(output))
    '''
    

    Returns
    -------
    None.

    '''
if __name__ == "__main__":
    app.run(debug=True)