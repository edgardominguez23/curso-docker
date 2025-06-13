from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json.get("data", [])
    return jsonify({"prediction": float(np.mean(data) if data else None)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)