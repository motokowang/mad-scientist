from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


from .database import Base


class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    