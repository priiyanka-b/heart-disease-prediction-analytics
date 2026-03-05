from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("heart_disease_model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"]) * 365
    gender = int(request.form["gender"])
    height = int(request.form["height"])
    weight = float(request.form["weight"])
    ap_hi = int(request.form["ap_hi"])
    ap_lo = int(request.form["ap_lo"])
    cholesterol = int(request.form["cholesterol"])
    gluc = int(request.form["gluc"])
    smoke = int(request.form["smoke"])
    alco = int(request.form["alco"])
    active = int(request.form["active"])

    bmi = weight / ((height / 100) ** 2)

    features = np.array([[age, gender, height, weight, ap_hi, ap_lo,
                          cholesterol, gluc, smoke, alco, active, bmi]])

    prediction = model.predict(features)

    result = "High Risk" if prediction[0] == 1 else "Low Risk"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)