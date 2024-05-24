from flask import request, jsonify
from config import app, db
from models import Books

@app.route("/", methods=["GET"])
def display():
    pass

@app.route("/books", methods=["GET"])
def display():
    books = Books.query.all()
    json_books = [book.to_json() for book in books]
    return jsonify({"books": json_books})

@app.route("/create_book", methods=["POST"])
def create_book():
    pass

@app.route("/update_book", methods=["put"])
def update_book():
    pass

@app.route("/update_book", methods=["DELETE"])
def update_book():
    pass


if __name__ == "__main__":
    app.run(debug=True)