import os 
import sqlite3

db=os.path.join(os.path.dirname(__file__),'site.db')
conn=sqlite3.connect(db,check_same_thread=False)
cur=conn.cursor()

def insert_record(name,email,password):
    cur.execute(
        "INSERT INTO user (name,email,password)VALUES(?,?,?)",(name,email,password))
    conn.commit()


def retrieve_user_password(email):
    cur.execute("SELECT password FROM user WHERE email= ?",(email,))

    row=cur.fetchall()

    return row




    

