import os
import json
import pandas as pd

DATA_DIR = "data"

def save_json(symbol: str, filename: str, data):
    """
    Lưu dữ liệu JSON vào thư mục tương ứng với mã cổ phiếu.
    """
    folder_path = os.path.join(DATA_DIR, symbol)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
