# import sqlite3
#
# db = sqlite3.connect("new-books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# with app.app_context():
#     db.create_all()
#
# with app.app_context():
#     book = Books(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(book)
#     db.session.commit()
#
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars().all()
    print(all_books)
