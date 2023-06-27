# import sqlite3
#
# conn = sqlite3.connect('test.db')

# conn.execute('''CREATE TABLE students (
#   id INTEGER PRIMARY KEY,
#   name VARCHAR(50),
#   age INTEGER
#  );  ''')
#
# conn.execute('INSERT INTO students (name,age) VALUES ("Osan",25);')
# conn.commit()
#
# conn.execute('UPDATE students SET name="Micael JAckson" WHERE id=1;')
# conn.commit()
#
# conn.execute('DELETE FROM students WHERE id=1;')
# conn.commit()
#
# result = conn.execute('SELECT * FROM students')
# for row in result:
#     print(row)
#
# conn.close()

# 1
# import sqlite3
#
# conn = sqlite3.connect('mydatabase.db')
#
# conn.execute('''DROP TABLE IF EXISTS teachers ''')
# conn.execute('''CREATE TABLE teachers (
#   id INTEGER PRIMARY KEY,
#   name VARCHAR(50)
#  );  ''')
#
# conn.execute('ALTER TABLE teachers ADD COLUMN subject;')
# conn.execute('INSERT INTO teachers (id, name,subject) VALUES (2, "Osan","math");')
# conn.commit()
# result = conn.execute('SELECT * FROM teachers')
# for row in result:
#     print(row)
#
# conn.close()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable=True)





with app.app_context():
    db.create_all()

    user = User(username='John')
    db.session.add(user)
    db.session.commit()


    user = User(username='Amir')
    db.session.add(user)
    db.session.commit()

    user = User(username='Morgen')
    db.session.add(user)
    db.session.commit()

    # user = User(username='John')
    # db.session.add(user)
    # db.session.commit()

    # post1 = Post(title="Lesson1", content="voivosjvjvj concsvbsvbbvhsbvvsdvsdv")
    #
    # db.session.add(post1)
    # db.session.commit()
    # posts = Post.query.all()
    # for post in posts:
    #     print(post.title)

    post1 = Post.query.filter_by(id=1).first()
    print(post1.title)
    post1.title = 'Updated Lesson1'
    db.session.commit()
    posts = Post.query.all()
    for post in posts:
        print(post.title)
    # users = User.query.all()
    # for user in users:
    #     print(user.username)

    # user = User.query.filter_by(username='John').first()
    # user.username = 'Jane'
    # db.session.commit()
    # print(user.username)
    #
    post = Post.query.filter_by(id=1).first()
    db.session.delete(post)
    db.session.commit()

    posts = Post.query.all()
    for post in posts:


