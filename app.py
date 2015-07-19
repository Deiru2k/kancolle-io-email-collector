from tornado.web import Application
from tornado.ioloop import IOLoop
from subscribe import EmailHandler
import sys

from database import db

routes = [
    ("/subscribe", EmailHandler),
]

app = Application(handlers=routes)

if __name__ == '__main__':

    db.generate_mapping(create_tables=True)

    if len(sys.argv) > 1: port = sys.argv[1]
    else: port = 8080

    try:
        app.listen(port=port)
        IOLoop.instance().start()
    except KeyboardInterrupt:
        sys.exit(0)
