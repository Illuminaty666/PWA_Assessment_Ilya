from flask import Flask, render_template
import sqlite3


app = Flask(__name__)
@app.route("/")
def home():
    
    db = sqlite3.connect(".database/reviews.db")
    db.row_factory = sqlite3.Row

    table = db.execute(f"SELECT uid,rating,game,comment,date FROM Reviews").fetchall()
    return render_template("index.html", table=table)

app.run(debug=True, port=5000)
