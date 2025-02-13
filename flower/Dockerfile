mkdir -p flower
cat <<EOL > flower/Dockerfile
FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "tasks", "flower", "--port=5555"]
EOL
