import pandas as pd
from datetime import datetime, timedelta

def clean_stock_data(df: pd.DataFrame):
    """Lọc bỏ dữ liệu lỗi, điền dữ liệu bị thiếu"""
    df = df.dropna()  # Xóa dữ liệu có giá trị NaN
    df = df[df["price"] > 0]  # Loại bỏ giá không hợp lệ
    return df

def calculate_moving_average(df: pd.DataFrame, window: int = 5):
    """Tính trung bình động giá cổ phiếu"""
    df[f"MA_{window}"] = df["price"].rolling(window=window).mean()
    return df

def detect_large_price_changes(df: pd.DataFrame, threshold: float = 5.0):
    """Phát hiện biến động giá lớn (tăng/giảm > threshold %)"""
    df["price_change"] = df["price"].pct_change() * 100
    return df[df["price_change"].abs() > threshold]

def calculate_financial_ratios(financial_data: dict):
    """Tính toán một số chỉ số tài chính cơ bản"""
    pe_ratio = financial_data["price"] / financial_data["eps"] if financial_data["eps"] else None
    roe = (financial_data["net_income"] / financial_data["equity"]) * 100 if financial_data["equity"] else None
    return {"P/E Ratio": pe_ratio, "ROE (%)": roe}

def process_stock_data(df: pd.DataFrame):
    """Tích hợp tất cả các bước xử lý dữ liệu"""
    df = clean_stock_data(df)
    df = calculate_moving_average(df)
    large_changes = detect_large_price_changes(df)
    return df, large_changes
