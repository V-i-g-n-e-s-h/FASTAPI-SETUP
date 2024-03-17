from sqlalchemy import Column, Enum, String, Integer
from database.database import base as Base
from database.db_enum import SampleTypes

class Sample(Base):
    __tablename__ = 'sample'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement="ignore_fk")
    name = Column(String)
    smple_enum = Column(Enum(SampleTypes), nullable=False)