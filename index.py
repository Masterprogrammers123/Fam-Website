from Sockets.server import main_program
from Sockets.client import main
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

bad_words = ["sex", 'balls','fuck', 'shit', 'bitch', 'nigga', 'nigger', 'fucking', 'pute', 'putain', 'merde', 'fucker', 'ass', 'asshole', 'dick', 'pussy', 'imbecile', 'imbécile'] # So we can blur the swearing when we setup the chat with **** or something
# We need to remember to put a .upper or .lower in the if statement that will check if there are any swear words

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
            flash("Account non existant.")
            return redirect(url_for("signup"))
    else:
       if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("chat"))
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out.")
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/views") # TODO: Delete this (IMPORTANT)
def view():
    return render_template("views.html", values=users.query.all())


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["Name"]
        email = request.form["Email"]
        password = request.form["Password"]
        usr = users(name, email, password)
        db.session.add(usr)
        db.session.commit()
    return render_template("signup.html") 

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

@app.route('/Erorrtest')
def erorr(Erorrtest):
    return '<h1>Erorr easter egg.</h1> Do u like furries. I certainly do. And wumpus. I do to.'       

""" # an approach of how we can blur the bad words
msg = input("hi!").lower()
for bad_word in bad_words:
    msg = msg.replace(bad_word, "*"*len(bad_word))
print(msg)
"""

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    
