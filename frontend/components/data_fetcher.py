import requests
from sqlalchemy.orm import Session
from models import StockPrice, StockInfo
from datetime import datetime

# API giả lập - Bạn có thể thay thế bằng API thật
API_BASE_URL = "https://api.example.com/stocks"

def fetch_stock_historical_data(symbol: str):
    """Lấy dữ liệu giá cổ phiếu theo ngày từ API"""
    url = f"{API_BASE_URL}/{symbol}/historical"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def fetch_stock_intraday_data(symbol: str):
    """Lấy dữ liệu giá cổ phiếu theo phút từ API"""
    url = f"{API_BASE_URL}/{symbol}/intraday"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def fetch_company_overview(symbol: str):
    """Lấy thông tin công ty từ API"""
    url = f"{API_BASE_URL}/{symbol}/overview"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def fetch_financial_report(symbol: str):
    """Lấy báo cáo tài chính từ API"""
    url = f"{API_BASE_URL}/{symbol}/financials"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def save_stock_price(db: Session, symbol: str, price: float):
    """Lưu dữ liệu giá cổ phiếu vào database"""
    stock_price = StockPrice(symbol=symbol, price=price, timestamp=datetime.utcnow())
    db.add(stock_price)
    db.commit()

def save_stock_info(db: Session, symbol: str, company_name: str, market_cap: float):
    """Lưu thông tin công ty vào database"""
    stock_info = StockInfo(symbol=symbol, company_name=company_name, market_cap=market_cap)
    db.add(stock_info)
    db.commit()
