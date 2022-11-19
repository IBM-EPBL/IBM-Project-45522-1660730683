import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
app = Flask(__name__)
model=pickle.load(open('CKD.pkl','rb'))

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
    
    test=[]
    if request.method == 'POST':
        test.append(request.form.get("AGE"))
        test.append(request.form.get("BLOOD_UREA"))
        test.append(request.form.get("BLOOD_GLUCOSE_RANDOM"))

        APPETITE=request.form.get("APPETITE")
        if APPETITE=='YES':
            test.append(1)
        else:
            test.append(0)
        ANEMIA=request.form.get("ANEMIA")
        if ANEMIA=='YES':
            test.append(1)
        else:
            test.append(0)
        CORONARY_ARTERY_DISEASE=request.form.get("CORONARY_ARTERY_DISEASE")
        if CORONARY_ARTERY_DISEASE=='YES':
            test.append(1)
        else:
            test.append(0)
        PUS_CELL=request.form.get("PUS_CELL")
        if PUS_CELL=='YES':
            test.append(1)
        else:
            test.append(0)
        RED_BLOOD_CELL=request.form.get("RED_BLOOD_CELL")
        if RED_BLOOD_CELL=='YES':
            test.append(1)
        else:
            test.append(0)
        DIABETES_MELLITUS=request.form.get("DIABETES_MELLITUS")
        if DIABETES_MELLITUS=='YES':
            test.append(1)
            
        else:
            test.append(0)
        PEDAL_EDEMA=request.form.get("PEDAL_EDEMA")
        if PEDAL_EDEMA=='YES':
            test.append(1)
        else:
            test.append(0)
    print(test)
    test_df=pd.DataFrame(test)
    test_df=np.array(test_df).reshape(1, -1)
    ans1=model.predict(test_df)
    ans2=model.predict(test_df)
    value=0
    if (ans1=='ckd'): value=1
    if value==1:
        answer1="Oops!! You are affected by CHRONIC KIDNEY DISEASE"
        return render_template('Result1.html',answer1=answer1,ans1=ans1,answer2=ans2)
    else:
        answer1="Happy to say, that you are not affected by CHRONIC KIDNEY DISEASE!!!"
        return render_template('Result.html',answer1=answer1,ans1=ans1,answer2=ans2)


if __name__ == '__main__':
    app.run(debug=True)
