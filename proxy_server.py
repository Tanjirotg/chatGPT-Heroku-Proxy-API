from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# check if the server is running


@app.route("/", methods=["GET"])
def ping():
    return "Hello, World!"

# call the OpenAI API


@app.route("/complete", methods=["POST"])
def complete():
    openai_api_key = request.headers.get("Authorization")
    response = requests.post(
        OPENAI_ENDPOINT,
        headers={"Authorization": openai_api_key},
        json=request.json
    )
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(port=5000)
