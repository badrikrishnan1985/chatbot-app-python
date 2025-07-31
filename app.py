import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
from flask import render_template
API_GATEWAY_URL = "https://your-api-id.execute-api.region.amazonaws.com/prod/chat"

@app.route("/chat", methods=["POST"])

@app.route("/")
def index():
    return render_template("chat.html")
def chat():
    user_input = request.json.get("message")
    response = requests.post(API_GATEWAY_URL, json={"message": user_input})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
