from flask import Flask,render_template, request
import joblib
import pandas as pd
#initialize the app
app1=Flask(__name__)
model=joblib.load("predict_79.pkl")

@app1.route('/')
def homepage():
    return render_template("home.html")
@app1.route('/contact')
def contact():
    return render_template("contact.html")

@app1.route('/dsa')
def dsa():
    return render_template("dsa.html")

@app1.route('/forms',methods=["GET","POST"])
def forms():
    return render_template("forms.html")
@app1.route('/predict',methods=["POST"])
def predict():
# preg: Number of times pregnant Integer 0–17

# plas: Plasma glucose concentration in a 2 h oral glucose tolerance testReal 0–199

# press: Diastolic blood pressure Real 0–122

# skin: Triceps skin fold thickness Real 0–992

# test: h serum insulin Real 0–846

# mass: Body mass index Real 0–67.1

# pedi: Diabetes pedigree function Real 0.078–2.42

# age: Age Integer 21–81
    preg=int(request.form.get("preg"))
    plas=float(request.form.get("plas"))
    press=float(request.form.get("press"))
    skin=float(request.form.get("skin"))
    test=float(request.form.get("test"))
    mass=float(request.form.get("mass"))
    pedi=float(request.form.get("pedi"))
    age=float(request.form.get("age"))
    result_of_prediction=model.predict([[preg,plas,press,skin,test,mass,pedi,age,]])  
    if result_of_prediction[0]==0:
        return "Patient is NOT DIABETIC <html><br><br><br><form method=\"POST\" action=\"/forms\"><button>Back to Forms</button></html>"
    else:
        return "Patient is DIABETIC <html><br><br><br><form method=\"POST\" action=\"/forms\"><button>Back to Forms</button></html>"
#running the app
app1.run(debug=True)