from app.router.router import Router, Handler
from app.server.routes import get_routes
from app.server.library_resource import LibraryResource
from app.library import Library
from app.server.server import run_server
from http.server import HTTPServer

if __name__ == "__main__":
    library = Library()
    library_resource = LibraryResource(library)
    routes = get_routes(library_resource)
    router = Router()

    for route in routes:
        router.add (route["method"], route["path"], route["call"])

    Handler.ROUTER = router
    run_server(HTTPServer, Handler)

    