#!/bin/bash

# Di chuyển đến thư mục backend (nếu cần)
cd "$(dirname "$0")"

# Chạy Uvicorn với số worker tối ưu hơn
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers 4
