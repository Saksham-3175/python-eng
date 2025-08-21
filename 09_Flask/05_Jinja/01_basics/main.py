from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def function():
    marks = {"Student1":7, 
             "Student2":4, 
             "Student3":9, 
             "Student4":3}
    return render_template("index.html", marks=marks)

app.run(debug=True)