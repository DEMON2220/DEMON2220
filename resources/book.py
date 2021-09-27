from models.books import Book
from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.books import Book, book_list


class BookListResource(Resource):

    def get(self):

        data = []

        for book in book_list:
            if book.is_publish is True:
                data.append(book.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        book = Book(title=data['title'],
                        description=data['description'],
                        author=data['author'])

        book_list.append(book)

        return book.data, HTTPStatus.CREATED
