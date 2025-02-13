# Sử dụng Node.js
FROM node:18-alpine

WORKDIR /app

# Copy package.json để cài đặt dependencies trước
COPY package.json package-lock.json ./
RUN npm install

# Copy toàn bộ frontend vào container
COPY . .

# Mở cổng mặc định của Next.js (nếu dùng Next.js)
EXPOSE 3000

# Chạy ứng dụng frontend
CMD ["npm", "run", "dev"]
