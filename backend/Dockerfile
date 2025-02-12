# Sử dụng Python 3.9 chính thức
FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file cần thiết trước để tối ưu caching layer
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Thiết lập biến môi trường tránh lỗi bytecode
ENV PYTHONUNBUFFERED=1

# Chạy Uvicorn với worker tối ưu
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
