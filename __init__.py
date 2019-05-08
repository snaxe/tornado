from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.web import Application
from tornado.ioloop import IOLoop
from controller import StudentsController,ClassController,TeacherController
from tornado_sqlalchemy import make_session_factory
from db.Schema import Schema
import os
from sqlalchemy import event,DDL
from models.Base import Base


define('port', default=9000, help='port to listen on')
factory = make_session_factory(os.environ.get('DATABASE_URL', 'postgresql://myuser:mypass@localhost/mydb'))

"""Creates initial schema"""
def create_schema():
    event.listen(Base.metadata, 'before_create', DDL("CREATE SCHEMA IF NOT EXISTS test_schema;"
                                                     "grant all privileges on schema test_schema to myuser;"
                                                     "grant all privileges on all tables in schema test_schema to myuser;"))
    Base.metadata.create_all(bind=factory.engine)

def main():
    app = Application([
        (r'/create',Schema),
        (r"/student/(\d+)",StudentsController.StudentsController),
        (r"/class/(\w+)", ClassController.ClassController),
        (r"/teacher/(\d+)", TeacherController.TeacherController),
    ],session_factory=factory,autoreload=True,debug=True)
    create_schema()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
