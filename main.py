from flask import Flask, render_template, request, session, redirect
from db import fetchdb, login

app = Flask(__name__)

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

    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
    
        user = login(username,password)
        if user:
           session['id'] = user['id']
           session['username'] = user['username']

           return redirect("/templates/add.html")

    return render_template("login.html")

@app.route("/templates/register.html")
def register():

    return render_template("register.html")


app.run(debug=True, port=5000)
