# Sử dụng Python 3.9
FROM python:3.9

# Cài đặt các thư viện cần thiết
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn backend vào container
COPY . .

# Mở cổng API FastAPI
EXPOSE 8000

# Chạy ứng dụng backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
