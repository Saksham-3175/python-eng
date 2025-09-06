from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path="/public", static_folder="static")
# app = Flask(__name__)

@app.route("/")
def home():
    return render_template(("index.html"))

app.run(debug=True)