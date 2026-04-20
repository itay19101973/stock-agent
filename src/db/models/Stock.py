from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True, nullable=False)

    users = relationship("UserStock", back_populates="stock")
