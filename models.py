import sqlite3 as sql
import os
ROOT = os.path.dirname(os.path.relpath((__file__)))

def create_post(name, content):
    conn = sql.connect(os.path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    conn.commit()
    conn.close()

def get_posts():
    conn = sql.connect(os.path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts