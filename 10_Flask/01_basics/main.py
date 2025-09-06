from flask import Flask, render_template

app = Flask(__name__) #creates a new flask app

@app.route("/") #decorator tells flask that whenever someones goes to "/", run the function below
def hello_world():
    return render_template("index.html")

app.run(debug=True)