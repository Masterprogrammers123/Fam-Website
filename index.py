from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import client

app = Flask(__name__)

@app.route("/")
def home():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)