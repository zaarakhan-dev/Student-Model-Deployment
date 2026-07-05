from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Student Performance Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    df = pd.DataFrame([data])

    
    df = df[
        [
            "gender",
            "race/ethnicity",
            "parental level of education",
            "lunch",
            "test preparation course",
            "math score",
            "reading score",
            "writing score",
            "Average score"
        ]
    ]

    prediction = model.predict(df)

    return jsonify({
        "Prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)