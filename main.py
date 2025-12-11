from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
def fetchdb():
    db = sqlite3.connect(".database/reviews.db")
    db.row_factory = sqlite3.Row

    return db

def login(user,pwd):
    db = fetchdb()

    un = db.execute("SELECT * FROM Users WHERE username=? COLLATE NOCASE", (user)).fetchone()

    if un != None:
        if (user['password'], pwd):
            return un
        
    return None

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/templates/add.html")
def add():

    return render_template("add.html")

@app.route("/templates/reviews.html")
def reviews():
    game = 'Hollow Knight'
    gamereviews = fetchdb()
    gamereviews = gamereviews.execute("SELECT * from Reviews").fetchall()
    return render_template("reviews.html", game=game, reviewtable=gamereviews)

@app.route("/templates/login.html", methods=['GET','POST'])
def login():

    return render_template("login.html")

@app.route("/templates/register.html")
def register():

    return render_template("register.html")


app.run(debug=True, port=5000)
