#!/bin/bash

# Di chuyển đến thư mục backend (nếu cần)
cd "$(dirname "$0")"

# Kiểm tra xem Redis hoặc RabbitMQ có chạy không trước khi khởi động worker
if ! nc -z localhost 6379; then
    echo "Redis chưa chạy! Vui lòng khởi động Redis trước."
    exit 1
fi

# Khởi động Celery worker
celery -A backend.celery worker --loglevel=info
