from flask import render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


# all_books = []


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = result.scalars().all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # all_books.append({"title": request.form['book_name'],
        #                   "author": request.form['book_author'],
        #                   "rating": request.form['rating']})
        with app.app_context():
            book = Books(title=request.form['book_name'], author=request.form['book_author'],
                         rating=request.form['rating'])
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        book_id = request.form['id']
        new_rating = float(request.form['new_rating'])

        with app.app_context():
            book_to_update = db.get_or_404(Books, book_id)
            book_to_update.rating = new_rating
            db.session.commit()

        return redirect(url_for('home'))

    else:
        bid = request.args.get('bid')
        with app.app_context():
            book = db.session.execute(db.select(Books).where(Books.id == bid)).scalar()
        return render_template('edit.html', book=book)


@app.route("/delete/<int:bid>", methods=['GET'])
def delete(bid):
    with app.app_context():
        book_to_delete = db.get_or_404(Books, bid)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
