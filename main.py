from flask import Flask, render_template, request, session, redirect
from db import fetchdb, loginverify, userreg, addreview

app = Flask(__name__)
app.secret_key = "gmreview"

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/templates/add.html", methods=['GET','POST'])
def add():

    if request.method == "POST":
        rating =  request.form['gamerating']
        comment = request.form['gamecomment']
        gname = request.form['gamename']
        user_id = session['id']

        if addreview(user_id,gname,comment,rating):
            return redirect("/templates/reviews.html")
    return render_template("add.html")
    

@app.route("/templates/reviews.html")
def reviews():
    game = 'Hollow Knight'
    gamereviews = fetchdb()
    gamereviews = gamereviews.execute("SELECT * from Reviews").fetchall()
    return render_template("reviews.html", reviewtable=gamereviews)

@app.route("/templates/login.html", methods=['GET','POST'])
def login():

    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
    
        user = loginverify(username,password)
        if user:
           session['id'] = user['id']
           session['username'] = user['username']

           return redirect("/templates/add.html")

    return render_template("login.html")

@app.route("/templates/register.html", methods=["GET","POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if userreg(username,password):
            return redirect("/templates/login.html")

    return render_template("register.html")


app.run(debug=True, port=5000)
