from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    rasa_response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",  # default Rasa endpoint
        json={"sender": "user", "message": user_message}
    )

    bot_messages = rasa_response.json()
    
    # Collect all messages sent by the bot (in case multiple responses are returned)
    if bot_messages:
        final_response = " ".join([msg.get("text", "") for msg in bot_messages])
    else:
        final_response = "Sorry, I didn't understand that."

    return jsonify({"response": final_response})

if __name__ == '__main__':
    app.run(debug=True)
