from sqlalchemy import create_engine, Float, Integer, String, Column, Date, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

db = create_engine('sqlite:///data.db')
Base = declarative_base(db=db)


class User(Base):
    __tablename__ = 'user'
    id = Column('id',Integer, primary_key=True)
    name = Column('name',String,nullable=False)

    created_at = Column('created_at',Date)
    status = Column('status',Boolean,default=True)

class Invoice(Base):
    __tablename__ = 'invoice'
    id = Column('id',Integer, primary_key=True)
    user = Column('cliente',ForeignKey('user.id'),nullable=False )
    created_at = Column('created_at',Date)
    price = Column('price',Float,nullable=False)

Base.metadata.create_all(bind=db)