from sqlalchemy import column, Integer, String, Date 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()   

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False)
    birthday = Column(Date, nullable=True)
    extra_info = Column(String, nullable=True)


