import os
import json
import csv
import requests
from sqlalchemy.orm import Session
from models import StockPrice

# Thư mục lưu dữ liệu xuất ra
EXPORT_FOLDER = "exported_data"

# Đảm bảo thư mục tồn tại
os.makedirs(EXPORT_FOLDER, exist_ok=True)

def export_to_csv(db: Session, symbol: str):
    """Xuất dữ liệu giá cổ phiếu ra file CSV"""
    prices = db.query(StockPrice).filter(StockPrice.symbol == symbol).all()
    file_path = os.path.join(EXPORT_FOLDER, f"{symbol}.csv")

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Symbol", "Price", "Timestamp"])
        for price in prices:
            writer.writerow([price.id, price.symbol, price.price, price.timestamp])

    return file_path

def export_to_json(db: Session, symbol: str):
    """Xuất dữ liệu giá cổ phiếu ra file JSON"""
    prices = db.query(StockPrice).filter(StockPrice.symbol == symbol).all()
    file_path = os.path.join(EXPORT_FOLDER, f"{symbol}.json")

    with open(file_path, "w") as file:
        json.dump([{"id": p.id, "symbol": p.symbol, "price": p.price, "timestamp": str(p.timestamp)} for p in prices], file)

    return file_path

def send_data_to_api(data, api_url):
    """Gửi dữ liệu đến API bên ngoài"""
    try:
        response = requests.post(api_url, json=data)
        return response.status_code, response.json()
    except Exception as e:
        return 500, {"error": str(e)}
