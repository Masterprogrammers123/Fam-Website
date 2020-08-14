from flask import Flask, redirect, url_for, render_template, request, session, flash
# Will import the socket stuff later

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) #no. U BRAT