
import sqlite3
from datetime import datetime
def fetchdb():
    db = sqlite3.connect(".database/reviews.db")
    db.row_factory = sqlite3.Row

    return db

def loginverify(username,password):
    db = fetchdb()

    un = db.execute("SELECT * FROM Users WHERE username=? COLLATE NOCASE", (username,)).fetchone()

    if un != None:
        if (un['password'], password):
            return un
        
    return None

def userreg(username, password):
    if username == None or password == None:
        return False
    
    db = fetchdb()
    db.execute("INSERT INTO Users(username,password) VALUES(?,?)", (username,password,))
    db.commit()
    return True

def addreview(uid,gname,comment,rating):
    
    if gname == None or rating < 0 or rating > 100:
        return False
    now = datetime.now()
    datestr = now.strftime("%d-%m-%y")
    db = fetchdb()
    db.execute("INSERT INTO Reviews(id,uid, game, rating, comment, date) VALUES(?,?,?,?,?)", (gname,uid,rating,comment,datestr,))
    db.commit()
    return True