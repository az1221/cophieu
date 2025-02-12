from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import StockPrice, StockInfo
from schemas import StockInfoResponse, StockPriceResponse

router = APIRouter()

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
