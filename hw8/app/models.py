from sqlalchemy import Column, Integer, String, Float, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    photo_data = Column(LargeBinary, nullable=True)
    
    purchases = relationship("Purchase", back_populates="user")

class Flower(Base):
    __tablename__ = "flowers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cost = Column(Float)
    
    purchases = relationship("Purchase", back_populates="flower")

class Purchase(Base):
    __tablename__ = "purchases"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flower_id = Column(Integer, ForeignKey("flowers.id"))
    
    user = relationship("User", back_populates="purchases")
    flower = relationship("Flower", back_populates="purchases")