from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class StockInfo(Base):
    __tablename__ = "stock_info"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    company_name = Column(String, nullable=False)
    market_cap = Column(Float, nullable=True)

    # Quan hệ với bảng StockPrice
    prices = relationship("StockPrice", back_populates="stock")

class StockPrice(Base):
    __tablename__ = "stock_prices"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, ForeignKey("stock_info.symbol"), nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=func.now())  # Lấy thời gian hiện tại

    # Liên kết với StockInfo
    stock = relationship("StockInfo", back_populates="prices")
