# Sử dụng Python 3.9 làm base image
FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file requirements để cài đặt dependencies
COPY flower/requirements.txt .

# Cài đặt thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép file tasks.py (hoặc backend/tasks.py nếu cần)
COPY backend/tasks.py .

# Chạy Flower UI
CMD ["celery", "-A", "tasks", "flower", "--port=5555"]
