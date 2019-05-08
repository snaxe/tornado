from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado_sqlalchemy import as_future
from models.Student import Student
import json
from .BaseController import BaseController
from models.Encoder import AlchemyEncoder



class StudentsController(BaseController):
    SUPPORTED_METHODS = ["GET"]

    @coroutine
    def get(self,studentId):
        with self.make_session() as session:
            student = yield as_future(session.query(Student).filter(Student.id == studentId).all)
            print(student)
            if student:
                self.send_response(json.dumps(student,cls=AlchemyEncoder))

