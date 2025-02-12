from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Stock Tracking System Backend"}

def test_get_stock_not_found():
    response = client.get("/stocks/INVALID")
    assert response.status_code == 200
    assert response.json() is None  # Vì không có dữ liệu trả về

def test_get_stock_prices_not_found():
    response = client.get("/prices/INVALID")
    assert response.status_code == 200
    assert response.json() == []  # Vì không có giá nào trả về
