import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

schema_posts = """
CREATE TABLE POSTS (
    id INTEGER primary key autoincrement,
    name text not null,
    content text not null
);
"""

cur.execute('DROP TABLE IF EXISTS posts;')
cur.execute(schema_posts)
conn.commit()
cur.close