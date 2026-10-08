from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

import joblib
import pandas as pd

app = Flask(__name__)

MODEL_FILE = "wireless_ids_model.pkl"


bundle = joblib.load(
    MODEL_FILE
)


model = bundle["model"]

features = bundle["features"]


print("AI model loaded successfully.")

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        data = request.get_json()


        values = {

            feature:
            float(data[feature])

            for feature in features

        }


        X = pd.DataFrame(

            [values],

            columns=features

        )

        prediction = int(

            model.predict(X)[0]

        )

        probabilities = model.predict_proba(X)[0]


        normal_probability = float(
            probabilities[0]
        )


        attack_probability = float(
            probabilities[1]
        )

        if prediction == 1:

            status = "INTRUSION DETECTED"

            severity = "HIGH"

        else:

            status = "NORMAL TRAFFIC"

            severity = "LOW"

        return jsonify({

            "success": True,

            "prediction": prediction,

            "status": status,

            "severity": severity,

            "normal_probability":
                round(
                    normal_probability * 100,
                    2
                ),

            "attack_probability":
                round(
                    attack_probability * 100,
                    2
                )

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)

        }), 400

if __name__ == "__main__":

    app.run(

        debug=True,

        host="127.0.0.1",

        port=8080

    )