from sqlalchemy.orm import Session
from models import StockPrice, StockInfo
from datetime import datetime

def add_stock_info(db: Session, symbol: str, company_name: str, market_cap: float):
    existing_stock = db.query(StockInfo).filter(StockInfo.symbol == symbol).first()
    if existing_stock:
        existing_stock.company_name = company_name
        existing_stock.market_cap = market_cap
    else:
        existing_stock = StockInfo(symbol=symbol, company_name=company_name, market_cap=market_cap)
        db.add(existing_stock)
    
    try:
        db.commit()
        db.refresh(existing_stock)
        return existing_stock
    except Exception as e:
        db.rollback()
        raise e  # Có thể log lỗi ở đây nếu cần

def add_stock_price(db: Session, symbol: str, price: float, timestamp: datetime):
    stock_price = StockPrice(symbol=symbol, price=price, timestamp=timestamp)
    db.add(stock_price)
    
    try:
        db.commit()
        db.refresh(stock_price)
        return stock_price
    except Exception as e:
        db.rollback()
        raise e  # Có thể log lỗi ở đây nếu cần
