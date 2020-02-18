from datetime import datetime
from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=true)
#
#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.datetime, nullable=False, default=datetime.utcnow)
#     content = b.Column(db.text, nullabule=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#
#     def __repr__(self):
#         return f"User('{self.tile}', '{self.date_posted}')"

# dummy data
posts = [
    {
        'author':'Ian Freed',
        'title':'First Post',
        'content':'Welcome to the blog!',
        'date_posted':'February 11, 2020'
    },
    {
        'author':'Ian Freed',
        'title':'Second Post',
        'content':'Blogs are hard!',
        'date_posted':'February 12, 2020'
    }
]

def getApp():
    retur app

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

if __name__ == '__main__':
    app.run(debug=True)
