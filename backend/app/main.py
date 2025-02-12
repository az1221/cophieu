from fastapi import FastAPI
from database import engine, Base
from routes import router
from fastapi.middleware.cors import CORSMiddleware

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
