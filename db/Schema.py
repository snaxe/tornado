from models.Student import Student
from models.Teacher import Teacher
from models.ClassRoom import ClassRoom
from controller.BaseController import BaseController


"""Populates data"""
class Schema(BaseController):

    def populate_data(self):
        with self.make_session() as session:
            students_1 = [Student(name='jack', email='ajck@gmail.com'),Student(name='sam', email='sam@gmail.com'),Student(name='john', email='john@gmail.com')]
            students_2 = [Student(name='peter', email='peter@gmail.com',contact='8736353'),Student(name='penelope', email='pen@gmail.com'),Student(name='sire', email='sire@gmail.com',contact='8736353')]
            students_1.extend(students_2)
            teachers = [Teacher(name='Amy',email='amy@tech.com',contact='09879899'),Teacher(name='Kimberley',email='kim@tech.com',contact='09879800'),
                        Teacher(name='Tiger',email='tg@tech.com',contact='988767')]
            classrooms = [ClassRoom(name='DS',teacher=teachers[0],students=students_1[:3]),
                          ClassRoom(name='DBMS',teacher=teachers[0],students=students_1[4:]),
                          ClassRoom(name='ML',teacher=teachers[1],students=students_1)]

            session.add_all(teachers) #Tiger would be missed. Hence adding it.
            session.add_all(classrooms)
            session.commit()

    def get(self):
        self.populate_data()