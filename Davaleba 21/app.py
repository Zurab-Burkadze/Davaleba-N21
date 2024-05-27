from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "Harry Potter and Philosopher's Stone", "author": "J.K Rowling", "year": 1997},
    {"id": 2, "title": "Harry Potter and Chamber of Secrets", "author": "J.K Rowling", "year": 1998},
    {"id": 3, "title": "Harry Potter and Prisoner of Azkaban", "author": "J.K Rowling", "year": 1999},
    {"id": 4, "title": "Harry Potter and Goblet of Fire", "author": "J.K Rowling", "year": 2000},
    {"id": 5, "title": "Harry Potter and Order of the Phoenix", "author": "J.K Rowling", "year": 2003},
    {"id": 5, "title": "Harry Potter and Half-Blood Prince", "author": "J.K Rowling", "year": 2005},
    {"id": 5, "title": "Harry Potter and Deathly Hallows", "author": "J.K Rowling", "year": 2007},
]



@app.route('/')
def home():
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>')
def book(book_id):
    for book in books:
        if book['id'] == book_id:
            return render_template('book.html', book=book)
    return 'Book not found', 404


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            "id": len(books) + 1,
            "title": request.form['title'],
            "author": request.form['author'],
            "year": int(request.form['year'])
        }
        books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)