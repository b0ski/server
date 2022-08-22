import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from app.library.library import Library, Book


class LibraryResource:
    _Library: Library = None

    def __init__(self, Library: Library):
        self._library = Library

    def add_book(self, req: BaseHTTPRequestHandler):
        self._Library.add_book(Book("Harry Potter", "Fantasy", "J.K. Rowling"))

        req.send_response(HTTPStatus.OK)
        req.send_header("Content-type", "application/json")
        req.end_headers()
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Andrey Varenyk', 'path': req.path,
                        'method': req.command, 'Library books': self._library.books.__str__()}).encode())
