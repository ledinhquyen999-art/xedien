from flask import Flask
import pandas as pd
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)

CREDS_PATH = "creds.json"
YOUR_EMAIL = "ledinhquyen999@gmail.com"   # Gmail của bạn


def upload_excel(file_path, file_name):
    scopes = ["https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file(CREDS_PATH, scopes=scopes)
    service = build("drive", "v3", credentials=creds)

    # Upload vào Drive của Service Account
    metadata = {"name": file_name}
    media = MediaFileUpload(
        file_path,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    uploaded = service.files().create(
        body=metadata,
        media_body=media,
        fields="id"
    ).execute()

    file_id = uploaded["id"]

    # Share lại file cho Gmail của bạn
    service.permissions().create(
        fileId=file_id,
        body={
            "type": "user",
            "role": "writer",
            "emailAddress": YOUR_EMAIL
        }
    ).execute()

    return file_id


@app.route("/")
def home():
    return "⚡ Flask đang chạy trên Render – Google Drive API OK!"


@app.route("/upload-test")
def upload_test():
    df = pd.DataFrame({
        "Time": ["10:00", "10:10", "10:20"],
        "Power": [12, 14, 15]
    })

    file_name = "test_upload.xlsx"
    df.to_excel(file_name, index=False)

    file_id = upload_excel(file_name, file_name)

    return f"✔ Upload thành công!<br>File ID: {file_id}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
