from flask import Flask, jsonify

app = Flask(__name__)

# Define Book class
class Book:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# Define Author class
class Author:
    def __init__(self, id, name, books):
        self.id = id
        self.name = name
        self.books = books  # list of Book objects

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "books": [book.to_dict() for book in self.books]
        }

# Sample data
authors = [
    Author(1, "Octavia Butler", [
        Book(1, "Kindred"),
        Book(2, "Parable of the Sower")
    ]),
    Author(2, "Toni Morrison", [
        Book(3, "Beloved"),
        Book(4, "Song of Solomon")
    ])
]

# GET /authors
@app.route("/authors")
def get_authors():
    return jsonify([author.to_dict() for author in authors])

# GET /authors/<int:id>
@app.route("/authors/<int:id>")
def get_author(id):
    author = next((a for a in authors if a.id == id), None)
    return jsonify(author.to_dict()) if author else ("Author not found", 404)

# GET /authors/<int:id>/books
@app.route("/authors/<int:id>/books")
def get_books_by_author(id):
    author = next((a for a in authors if a.id == id), None)
    return jsonify([book.to_dict() for book in author.books]) if author else ("Author not found", 404)

# GET /authors/<int:author_id>/books/<int:book_id>
@app.route("/authors/<int:author_id>/books/<int:book_id>")
def get_book_by_author(author_id, book_id):
    author = next((a for a in authors if a.id == author_id), None)
    if not author:
        return ("Author not found", 404)
    book = next((b for b in author.books if b.id == book_id), None)
    return jsonify(book.to_dict()) if book else ("Book not found", 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
