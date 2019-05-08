from sqlalchemy import *
from .Base import Base
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = "teachers"
    __table_args__ = {'schema': 'test_schema'}
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column('email', String(60))
    contact = Column('contact', String(15))
    classes = relationship("ClassRoom", back_populates="teacher")

    def __str__(self):
        return f"{self.id} {self.name} {self.email} {self.contact}"