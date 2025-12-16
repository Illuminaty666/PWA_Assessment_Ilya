
import sqlite3
def fetchdb():
    db = sqlite3.connect(".database/reviews.db")
    db.row_factory = sqlite3.Row

    return db

def loginverify(username,password):
    db = fetchdb()

    un = db.execute("SELECT * FROM Users WHERE username=? COLLATE NOCASE", (username,)).fetchall()

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