from Sockets.server import main_program
from Sockets.client import main
from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def home():
    return render_template("index.html")

@app.route('/main')
@app.route("/chat")
def chat():
    return render_template("chat.html")
@app.route('/TOS')
def rules():
    return render_template('Tos.html') 
@app.route('/Erorrtest')
def erorr():
    return 'Erorr easter egg. Do u like furries. I certainly do. And wumpus. I do to.'       

if __name__ == "__main__":
    app.run(debug=True)                        