# Sử dụng Python 3.9 làm base image
FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY flower/requirements.txt /app/requirements.txt

# Cài đặt thư viện cần thiết
RUN pip install --no-cache-dir -r /app/requirements.txt

# Sao chép toàn bộ thư mục backend vào container
COPY backend /app/backend

# Đặt thư mục backend vào PYTHONPATH
ENV PYTHONPATH=/app/backend

# Chạy Flower UI
CMD ["celery", "-A", "backend.tasks", "flower", "--port=5555"]
