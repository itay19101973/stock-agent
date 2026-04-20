from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class UserStock(Base):
    __tablename__ = "user_stocks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    stock_id = Column(Integer, ForeignKey("stocks.id"))

    user = relationship("User", back_populates="stocks")
    stock = relationship("Stock", back_populates="users")