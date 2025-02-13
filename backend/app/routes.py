from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import StockPrice, StockInfo
from schemas import StockInfoResponse, StockPriceResponse
import vnstock
from fastapi import APIRouter
from datetime import datetime, timedelta
from .utils import save_json
from typing import List
import json
import os

router = APIRouter()

WATCHLIST_FILE = "data/watchlist.json"

def load_watchlist():
    if os.path.exists(WATCHLIST_FILE):
        with open(WATCHLIST_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_watchlist(watchlist):
    with open(WATCHLIST_FILE, "w", encoding="utf-8") as f:
        json.dump(watchlist, f, indent=4)

@router.get("/watchlist")
def get_watchlist():
    return load_watchlist()

@router.post("/watchlist/add")
def add_to_watchlist(symbol: str):
    watchlist = load_watchlist()
    if symbol not in watchlist:
        watchlist.append(symbol)
        save_watchlist(watchlist)
    return {"message": f"Đã thêm {symbol} vào danh sách theo dõi."}

@router.delete("/watchlist/remove")
def remove_from_watchlist(symbol: str):
    watchlist = load_watchlist()
    if symbol in watchlist:
        watchlist.remove(symbol)
        save_watchlist(watchlist)
    return {"message": f"Đã xóa {symbol} khỏi danh sách theo dõi."}
    

@router.get("/stocks/{symbol}", response_model=StockInfoResponse)
def get_stock(symbol: str, db: Session = Depends(get_db)):
    stock = db.query(StockInfo).filter(StockInfo.symbol.ilike(symbol)).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.get("/prices/{symbol}", response_model=list[StockPriceResponse])
def get_stock_prices(symbol: str, db: Session = Depends(get_db)):
    prices = db.query(StockPrice).filter(StockPrice.symbol.ilike(symbol)).all()
    if not prices:
        raise HTTPException(status_code=404, detail="No price data found for this stock")
    return prices

@router.get("/stocks", response_model=list[StockInfoResponse])
def get_all_stocks(db: Session = Depends(get_db)):
    stocks = db.query(StockInfo).all()
    return stocks
