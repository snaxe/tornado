from tornado_sqlalchemy import SessionMixin
from tornado.web import RequestHandler

class BaseController(RequestHandler, SessionMixin):

    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def send_response(self, data, status=200):
        self.set_status(status)
        self.write(data)