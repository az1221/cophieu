mkdir -p scripts  # Tạo thư mục scripts nếu chưa có
cat <<EOL > scripts/setup.sh
#!/bin/bash

echo "🚀 Bắt đầu kiểm tra frontend..."

# Kiểm tra nếu node_modules chưa tồn tại thì mới cài đặt
if [ ! -d "/app/frontend/node_modules" ]; then
    echo "📦 Chưa cài đặt frontend, tiến hành cài đặt..."
    cd /app/frontend && npm install
else
    echo "✅ Frontend đã được cài đặt, bỏ qua bước cài đặt."
fi

echo "🎉 Hoàn thành kiểm tra frontend!"
EOL
