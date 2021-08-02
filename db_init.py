from dotenv import load_dotenv
# .envファイルの内容を読み込みます
load_dotenv()

import os

import sqlite3

dbname = os.environ["DBNAME"]
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('CREATE TABLE instagramContents(id INTEGER PRIMARY KEY AUTOINCREMENT, post_content STRING);')
conn.commit()
conn.close()