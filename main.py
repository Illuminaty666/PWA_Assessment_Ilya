from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

@app.route("/")
def home():
    
    db = sqlite3.connect(".database/reviews.db")
    db.row_factory = sqlite3.Row

    table = db.execute(f"SELECT uid,rating,game,comment,date FROM Reviews").fetchall()
    return render_template("index.html", table=table)

@app.route("/templates/add.html")
def add():

    return render_template("add.html")

@app.route("/templates/reviews.html")
def reviews():
    game = 'Hollow Knight'
    return render_template("reviews.html", game=game)

@app.route("/templates/login.html")
def login():
    db = sqlite3.connect(".database/reviews.db")
    db.row_factory = sqlite3.Row 

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
    usertable = db.execute(f"SELECT * from Users").fetchall() 


    return render_template("login.html", table=usertable)

@app.route("/templates/register.html")
def register():
    return render_template("register.html")


app.run(debug=True, port=5000)
