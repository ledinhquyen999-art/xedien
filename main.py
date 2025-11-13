from flask import Flask, send_file
import pandas as pd
import os

app = Flask(__name__)

# Tạo thư mục data nếu chưa có
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/")
def home():
    return "Server đang chạy OK trên Render!"

@app.route("/save-test")
def save_test():
    # Tạo DataFrame
    df = pd.DataFrame({
        "Time": ["10:00", "11:00", "12:00"],
        "Power": [10, 12, 14]
    })

    file_path = os.path.join(DATA_DIR, "today.xlsx")
    df.to_excel(file_path, index=False)

    return f"Đã lưu file Excel thành công tại: {file_path}"

@app.route("/download")
def download():
    file_path = os.path.join(DATA_DIR, "today.xlsx")
    if not os.path.exists(file_path):
        return "Chưa có file. Hãy gọi /save-test trước."

    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

