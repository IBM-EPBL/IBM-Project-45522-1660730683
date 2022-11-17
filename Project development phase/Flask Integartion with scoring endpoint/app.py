import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "xiMVDb4L5mvINXcJ2991XUc8UF-5ILsZp-nMFjTk4CjQ"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home page.html')

@app.route('/bmi')
def bmi():
    return render_template('Calculator.html')

@app.route('/information')
def information():
    return render_template('Information.html')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/result',methods=['POST'])
def predict():
    AGE=request.form["AGE"]
    BLOOD_UREA=request.form["BLOOD_UREA"]
    BLOOD_GLUCOSE_RANDOM = request.form["BLOOD_GLUCOSE_RANDOM"]
    APPETITE=request.form["APPETITE"]
    ANEMIA=request.form["ANEMIA"]
    CORONARY_ARTERY_DISEASE=request.form["CORONARY_ARTERY_DISEASE"]
    PUS_CELL=request.form["PUS_CELL"]
    RED_BLOOD_CELL=request.form["RED_BLOOD_CELL"]
    DIABETES_MELLITUS=request.form["DIABETES_MELLITUS"]
    PEDAL_EDEMA=request.form["PEDAL_EDEMA"]

    if APPETITE=='YES':
        APPETITE=1
    if APPETITE=='NO':
        APPETITE=0

    
    if ANEMIA=='YES':
        ANEMIA=1
    if ANEMIA=='NO':
        ANEMIA=0

    
    if CORONARY_ARTERY_DISEASE=='YES':
        CORONARY_ARTERY_DISEASE = 1
    if CORONARY_ARTERY_DISEASE=='NO':
        CORONARY_ARTERY_DISEASE=0

    
    if PUS_CELL=='YES':
        PUS_CELL=1
    if PUS_CELL=='NO':
        PUS_CELL=0

    
    if RED_BLOOD_CELL=='YES':
        RED_BLOOD_CELL=1
    if RED_BLOOD_CELL=='NO':
        RED_BLOOD_CELL=0

    
    if DIABETES_MELLITUS=='YES':
        DIABETES_MELLITUS=1
    if DIABETES_MELLITUS=='NO':
        DIABETES_MELLITUS=0

    
    if PEDAL_EDEMA=='YES':
        PEDAL_EDEMA=1
    if PEDAL_EDEMA=='NO':
        PEDAL_EDEMA=0
    t=[int(AGE),int(BLOOD_UREA),int(BLOOD_GLUCOSE_RANDOM),int(APPETITE),int(ANEMIA),int(CORONARY_ARTERY_DISEASE),int(PUS_CELL),int(RED_BLOOD_CELL),int(DIABETES_MELLITUS),int(PEDAL_EDEMA)]
    print(t)
    payload_scoring = {"input_data": [{"fields": [ "AGE","BLOOD_UREA","BLOOD_GLUCOSE_RANDOM","APPETITE","ANEMIA","CORONARY_ARTERY_DISEASE","PUS_CELL","RED_BLOOD_CELL","DIABETES_MELLITUS","PEDAL_EDEMA"], "values": [t]}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/cbc0e58e-0b2c-4ce7-884b-0a602d282d57/predictions?version=2022-11-16', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions=response_scoring.json()
    print(predictions)
    val=0
    pred=predictions['predictions'][0]['values'][0][0]
    print(pred)
    if (pred =='ckd'): val=1
    if(val==1):
        output="Oops!! You are affected by CHRONIC KIDNEY DISEASE"
        print("Oops!! You are affected by CHRONIC KIDNEY DISEASE")
        return render_template('Result1.html',predictions_text=output)
    else:
        output="Happy to say, that you are not affected by CHRONIC KIDNEY DISEASE!!!"
        print("Happy to say, that you are not affected by CHRONIC KIDNEY DISEASE!!!")
        return render_template('Result.html',predictions_text=output)

if __name__ == '__main__':
    app.run(debug=True)