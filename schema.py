import os
import sqlite3

db=os.path.join(os.path.dirname(__file__),'site.db')

conn=sqlite3.connect(db)


cursor=conn.cursor()


cursor.execute(
"""
CREATE TABLE user(
    id INT,
    name VARCHAR(25),
    email VARCHAR(80),
    password TEXT,

    PRIMARY KEY (id)
);

""")

conn.close()