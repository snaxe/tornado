from .BaseController import BaseController
from tornado.gen import coroutine
from tornado_sqlalchemy import as_future
from models.ClassRoom import *
from models.Encoder import AlchemyEncoder
import json

class ClassController(BaseController):
    SUPPORTED_METHODS = ("GET")

    @coroutine
    def get(self,classname):
        with self.make_session() as session:
            classroom = yield as_future(session.query(ClassRoom).filter(ClassRoom.name == classname).all)
            if classroom:
                self.send_response(json.dumps(classroom,cls=AlchemyEncoder))

