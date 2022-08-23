from app.router.router import Router, Handler
from app.server.routes import get_routes
from app.server.library_resource import LibraryResource
from app.library.library import Library
from app.server.server import run_server
from http.server import HTTPServer
import psycopg2
from config import host, user, password, db_name

try:
    # connect to the database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        datebase=db_name
    )

    # the cursor for database operations
    with connection.cursor() as cursor:
        pass

except Exception as _ex:
    print("[INFO] Error while working with PostgresSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgresSQL connection is closed", _ex)


if __name__ == "__main__":
    library = Library('address', 'telephone', [], [])
    library_resource = LibraryResource(library)
    routes = get_routes(library_resource)
    router = Router()

    for route in routes:
        router.add (route["method"], route["path"], route["call"])

    Handler.ROUTER = router
    run_server(HTTPServer, Handler)

