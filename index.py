from Sockets.server import main_program
from Sockets.client import main
from flask import Flask, redirect, url_for, render_template, request, session, flash
from time import sleep
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

bad_words = ["sex", 'balls','fuck', 'shit', 'bitch', 'nigga', 'nigger', 'fucking', 'pute', 'putain', 'merde', 'fucker', 'ass', 'asshole', 'dick', 'pussy', 'imbecile', 'imbécile'] # So we can blur the swearing when we setup the chat with **** or something

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "SeCreTkEyOfApPnOtToBeGuEsSeSdhisdusiudtsougusuo"
app.permanent_session_lifetime = timedelta(days=365)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
class messages(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    message = db.Column(db.String(5000))
    day_sent = db.Column(db.String(10))
    time_sent = db.Column(db.String(5)) # Has to be a String because 23:59 isint an integer
    def __init__(self, message, day_sent, time_sent):
        self.message = message
        self.day_sent = day_sent
        self.time_sent = time_sent

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        signup_name = request.form["Name"]
        email = request.form["Email"]
        password = request.form["Password"]
        usr = users(signup_name, email, password)
        db.session.add(usr)
        db.session.commit()
        sleep(10)
        flash("Signed up.")
        return redirect(url_for('home'))
    return render_template("signup.html") 

signup_name = None
@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session.permanent = True
        login_email = request.form["loginemail"]
        login_pass = request.form["loginpass"]
        login_user = login_email + ' ' + login_pass
        found_user = users.query.filter_by(email=login_email, password=login_pass).first()
        if found_user:
            session["user"] = login_user
            flash("Logged In.")
            return redirect(url_for("chat"))
        else:
            flash("Wrong username/password")
            return redirect(url_for("home"))
    else:
       if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("chat"))
    return render_template("index.html")

signup_name = None

@app.route("/logout")
def logout():
    if 'user' in session:
        flash("You have been logged out.")
        session.pop("user", None)
        return redirect(url_for("home"))
    else:
        flash("Not logged in")
        return redirect(url_for("home"))

@app.route('/main', methods=["GET", 'POST'])
@app.route("/chat", methods=["GET", 'POST'])
def chat():
    if 'user' not in session:
        flash("Not logged in.")
        return redirect(url_for("home"))
    return render_template("chat.html")

@app.route("/TermsOfService")
@app.route('/TOS')
@app.route("/tos")
@app.route("/Tos")
def rules():
    return render_template('TOS.html')

@app.route('/Erorrtest')
def erorr(Erorrtest):
    return '<h1>Erorr easter egg.</h1> Do u like furries. I certainly do. And wumpus. I do to.'       

def stuff():
    print('stuff')

""" # an approach of how we can blur the bad words
msg = input("hi!").lower()
for bad_word in bad_words:
    msg = msg.replace(bad_word, "*"*len(bad_word))
print(msg)
"""

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", debug=True) # host for repl.it (To be changed)
    
