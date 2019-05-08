from tornado.gen import coroutine
from tornado_sqlalchemy import as_future
from models.Teacher import Teacher
import json
from .BaseController import BaseController
from models.Encoder import AlchemyEncoder



class TeacherController(BaseController):
    SUPPORTED_METHODS = ["GET"]

    @coroutine
    def get(self,teacher_id):
        with self.make_session() as session:
            classroom = yield as_future(session.query(Teacher).filter(Teacher.id == teacher_id).all)
            if classroom:
                self.send_response(json.dumps(classroom,cls=AlchemyEncoder))

