from sqlalchemy import *
from .Base import Base
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import json


association_table = Table('association', Base.metadata,
                          Column('class', Integer, ForeignKey('test_schema.classes.id')),
                          Column('student', Integer, ForeignKey('test_schema.students.id')))


class ClassRoom(Base):
    __tablename__ = "classes"
    __table_args__ = {'schema': 'test_schema'}
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    teacher_id = Column(Integer, ForeignKey('test_schema.teachers.id'))
    teacher = relationship("Teacher", back_populates="tclass",lazy='select')
    students = relationship("Student",secondary=association_table,back_populates="classroom")


    def __str__(self):
        return f"{self.id} {self.name} {self.teacher} {self.students}"