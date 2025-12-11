from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

def getdb():
    dtb = sqlite3.connect(reviews.db)
    dtb.row_factory = sqlite3.Row # Allows accessing rows by column name
    return dtb

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

    return render_template("reviews.html")

@app.route("/templates/login.html", methods=["POST"])
def login():
    db = sqlite3.connect(".database/reviews.db")
    db.row_factory = sqlite3.Row 

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
    usertable = db.execute(f"SELECT * from Users WHERE username = ? AND password= ?", (username,password)).fetchone()

    
    return render_template("login.html", table=usertable)

app.run(debug=True, port=5000)
