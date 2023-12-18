import sqlite3


def query(type,command):  
    con = sqlite3.connect('app/database/db.db')
    cur = con.cursor()
    if type=='get':
        response = cur.execute(command).fetchall()
        con.close()
        return response
    if type=='set':
        cur.execute(command)
        con.commit()
        lastRecord = cur.lastrowid
        con.close()
        return lastRecord

def createTable():
    exist = query('get',"""SELECT name FROM sqlite_master WHERE type='table' AND name='ads'; """)
    if not exist:
        print('creating table')
        query('get', """ CREATE TABLE ads(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                label TEXT NOT NULL,
                textContent TEXT NOT NULL)""")
    else:
        print('table exists')



