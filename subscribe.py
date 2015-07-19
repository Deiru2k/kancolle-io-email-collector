from pony.orm import db_session
from tornado.gen import coroutine
from tornado.web import RequestHandler
from models import Subscription


class EmailHandler(RequestHandler):

    def set_default_headers(self):

        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST"
        }
        for key in headers:
            self.set_header(key, headers[key])

    @coroutine
    def post(self):

        with db_session:

            email = self.get_argument("email")
            subscription = Subscription.get(email=email)
            if subscription:
                self.set_status(409)
                self.finish()
                return
            Subscription(email=email)
            self.set_status(201)
            self.finish()
            return
