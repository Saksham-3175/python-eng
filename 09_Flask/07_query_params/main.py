from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def query_params():
    name = "Default"
    token = "0000"
    
    if "name" in request.args.keys():
        name = request.args['name']
    if "tokens" in request.args.keys():
        token = request.args['tokens']
    return render_template("index.html", name=name, token=token)

app.run(debug=True)
