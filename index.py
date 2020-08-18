from Sockets.server import main_program
from Sockets.client import main
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

bad_words = ['balls','fuck', 'shit', 'bitch', 'nigga', 'nigger', 'fucking', 'pute', 'putain', 'merde', 'fucker', 'ass', 'asshole', 'dick', 'pussy', 'imbecile', 'imbécile'] # So we can blur the swearing when we setup the chat with **** or something
# We need to remember to put a .upper or .lower in the if statement that will check if there are any swear words

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def home():
    return render_template("index.html")

@app.route('/main')
@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/TermsOfService")
@app.route('/TOS')
@app.route("/tos")
@app.route("/Tos")
def rules():
    return render_template('TOS.html')

@app.route('/<Erorrtest>')
def erorr(Erorrtest):
    return '<h1>Erorr easter egg.</h1> Do u like furries. I certainly do. And wumpus. I do to.'       

""" # an approach of how we can blur the bad words
msg = input("hi!")
for bad_word in bad_words:
    msg = msg.replace(bad_word, "*"*len(bad_word))
print(msg)
"""

if __name__ == "__main__":
    app.run(debug=True)
    