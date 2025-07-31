from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def chatbot_response(message):
    if 'hello' in message.lower():
        return "Hi there! How can I help you?"
    elif 'bye' in message.lower():
        return "Goodbye! Have a great day."
    else:
        return "I'm a simple bot. You said: " + message

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
