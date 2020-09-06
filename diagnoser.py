from flask import Flask, request
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hi There</h1> <br> <h3>This is a simple webapp that diagnoses (identify) an individual with diabetes or not. <br> This is an awesome application of Machine Learning and Artificial Intelligence </h3>"

@app.route("/diagnose", methods=["POST"])
def diagnose():
    pregnancies = request.form["pregnancies"]
    glucose = request.form["glucose"]
    bp = request.form["bp"]
    st = request.form["st"]
    insulin = request.form["insulin"]
    bmi = request.form["bmi"]
    dpf = request.form["dpf"]
    age = request.form["age"]

    arr = np.array([[pregnancies, glucose, bp, st, insulin, bmi, dpf, age]])
    pred = model.predict(arr)[0]
    prob = model.predict_proba(arr)[:,1][0]
    return {
        "prediction": str(pred),
        "probability": str(prob)
    }


if __name__ == "__main__":
    app.run(debug=True)