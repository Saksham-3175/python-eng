from flask import Flask, jsonify

app = Flask(__name__)

marks = {
    "name1":20,
    "name2":53,
    "name3":70,
    "name4":28,
    "name5":89,
         }
vlaues = ["Name", "id", "passworld", 31]
@app.route("/")
def json():
    return jsonify(vlaues)

app.run(debug=True)