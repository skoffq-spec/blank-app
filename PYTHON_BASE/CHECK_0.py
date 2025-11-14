from sqlalchemy import *
from sqlalchemy import orm
from sqlalchemy.orm import *

Base = declarative_base()

class service(Base):    
    __tablename__ = "service"
    id_service = Column(Integer,primary_key=True)
    name = Column(VARCHAR)
    price = Column(Integer)
    
class Client(Base):
    __tablename__ = 'client'
    id_client = Column(Integer,primary_key=True)
    surname = Column(VARCHAR)
    name = Column(VARCHAR)
    patronymic =Column(VARCHAR)    
    phone = Column(Integer)
    
class Stock(Base):
    __tablename__ = 'stock'
    id_stock = Column(Integer,primary_key=True)
    dascrition = Column(VARCHAR)
    discount = Column(Integer)
    
class Gift(Base):
    __tablename__ = 'gift'
    id_gift = Column(Integer,primary_key=True)
    dascription = Column(VARCHAR)

class Change(Base):
    __tablename__ = 'change'
    id_change = Column(Integer,primary_key=True)
    dascription = Column(VARCHAR)

class Worker(Base):
    __tablename__ = 'worker'
    id_worker = Column('id_worker',Integer,primary_key=True)
    surname = Column('surname',VARCHAR)
    name = Column('name',VARCHAR)
    patronymic = Column('patronymic',VARCHAR)
    passport_info = Column('passport_info',VARCHAR)
    address = Column('address',VARCHAR)
    phone = Column('phone',Integer)
    salary = Column(Integer)
    change = Column(Integer,ForeignKey('change.id_change'))
    post = Column(VARCHAR)
    
class Schedule(Base):
    __tablename__ = 'schedule'
    id_schedule = Column('id_schedule',Integer,primary_key=True)
    data = Column('data',Date)
    time = Column('time',Time)
    service = Column(Integer,ForeignKey('service.id_service'))
    worker = Column(Integer,ForeignKey('worker.id_worker'))
    clien = Column(Integer,ForeignKey('client.id_client'))
    stock = Column(Integer,ForeignKey('stock.id_stock'))
    gift = Column(Integer,ForeignKey('gift.id_gift'))

if __name__ == '__main__':
    engine = create_engine('sqlite:///project_db.sqlite3')
    Base.metadata.create_all(engine)
