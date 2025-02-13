from fastapi import FastAPI
from database import engine, Base
from routes import router
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import sys

try:
    import vnstock
except ImportError:
    print("vnstock chưa được cài đặt. Đang tiến hành cài đặt từ GitHub...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/thinh-vu/vnstock.git"])
    import vnstock  # Import lại sau khi cài đặt thành công

# Khởi tạo database
Base.metadata.create_all(bind=engine)

# Tạo ứng dụng FastAPI
app = FastAPI()

# Cấu hình CORS (cho phép frontend truy cập API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Chấp nhận tất cả domain (có thể giới hạn theo yêu cầu)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký API routes
app.include_router(router)

# Route mặc định để kiểm tra API hoạt động
@app.get("/")
def read_root():
    return {"message": "Stock Tracking System Backend"}
