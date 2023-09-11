from datatime import  datatime
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, DataTime


Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primamry_key= True)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    birth = Column(DateRime)
    created = Column(DataTime, default = datatime.utcnow)
