from sqlalchemy import create_engine , func
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship , backref
from datetime import date




engine = create_engine('postgresql://postgres:Spudsinhel1@localhost:5432/password_management')
Session = sessionmaker(bind=engine)
Base = declarative_base()



