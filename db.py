
import sqlite3
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
