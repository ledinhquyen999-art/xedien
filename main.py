from flask import Flask

# Tạo ứng dụng Flask
app = Flask(__name__)

# Trang chủ
@app.route('/')
def home():
    return "🚀 Xin chào! Ứng dụng Flask của bạn đã chạy thành công trên Render!"

# Chạy server khi khởi động
if __name__ == '__main__':
    # Render cần host='0.0.0.0' và port=10000
    app.run(host='0.0.0.0', port=10000)
