from flask import Flask
import os
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Path secret file (Render sẽ mount vào /etc/secrets/)
CREDS_PATH = "creds.json"
FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

def upload_excel_to_drive(file_path, file_name):
    scopes = ["https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_PATH, scopes)
    service = build("drive", "v3", credentials=creds)

    metadata = {
        "name": file_name,
        "parents": [FOLDER_ID]
    }

    media = MediaFileUpload(
        file_path,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    uploaded = service.files().create(
        body=metadata,
        media_body=media,
        fields="id"
    ).execute()

    return uploaded.get("id")


@app.route("/")
def home():
    return "🌿 Flask đang chạy trên Render – API Drive OK"


@app.route("/upload-test")
def upload_test():
    # Tạo file Excel mẫu
    df = pd.DataFrame({
        "Time": ["10:00", "10:05", "10:10"],
        "Power (kW)": [12, 14, 15]
    })

    test_file = "test_upload.xlsx"
    df.to_excel(test_file, index=False)

    # Upload lên Drive
    file_id = upload_excel_to_drive(test_file, "test_upload.xlsx")

    return f"Đã upload thành công test_upload.xlsx!<br>File ID: {file_id}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

