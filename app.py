from flask import Flask, jsonify, request

from inference import predict

app = Flask(__name__)


@app.route("/api/relevancy", methods=["POST"])
def api():
    data = request.get_json()
    text = data["text"]

    if not text:
        return jsonify({"error": "No text provided"}), 400

    return jsonify({"relevancy": predict(text)})
