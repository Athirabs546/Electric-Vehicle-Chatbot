from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import csv
import sqlite3
import requests

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session management

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    rasa_response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": user_message}
    )

    bot_messages = rasa_response.json()
    final_response = " ".join([msg.get("text", "") for msg in bot_messages]) if bot_messages else "Sorry, I didn't understand that."
    return jsonify({"response": final_response})

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('admin.db')
        c = conn.cursor()
        c.execute("SELECT * FROM admin_users WHERE username=? AND password=?", (username, password))
        admin = c.fetchone()
        conn.close()
        if admin:
            session['admin_logged_in'] = True
            return redirect('/admin')
        else:
            error = "Invalid credentials"
    return render_template('login.html', error=error)

@app.route('/admin')
def admin_panel():
    if not session.get('admin_logged_in'):
        return redirect('/login')
    user_data = []
    with open('user_data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            user_data.append(row)
    return render_template('admin.html', user_data=user_data)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
