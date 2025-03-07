from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = "member"

    user_id = Column(String(15), primary_key=True, index=True)  # VARCHAR(15) PRIMARY KEY
    email = Column(String(20), unique=True, nullable=False)  # VARCHAR(20) NOT NULL UNIQUE
    password = Column(String(15), nullable=False)  # VARCHAR(15) NOT NULL
    name = Column(String(10), nullable=False)  # VARCHAR(10) NOT NULL


