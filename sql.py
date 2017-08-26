#our database has table posts with two fields -title and post
import sqlite3

with sqlite3.connect("blog.db") as connection:

    c=connection.cursor()

    c.execute("""CREATE TABLE posts
                (title TEXT,post TEXT)
              """)
    c.execute('INSERT INTO posts values("Good","I\'m good")')

    c.execute('INSERT INTO posts values("Well","I\'m well")')

    c.execute('INSERT INTO posts values("Excellent","I\'m excellent")')

    c.execute('INSERT INTO posts values("Okay","I\'m okay")')
    
    

    
