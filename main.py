from flask import Flask
import os
import pandas as pd

from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build

app = Flask(__name__)

CREDS_PATH = "creds.json"
FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")


def upload_excel_to_drive(file_path, file_name):
    scopes = ["https://www.googleapis.com/auth/drive.file"]

    creds = Credentials.from_service_account_file(
        CREDS_PATH,
        scopes=scopes
    )

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

    return uploaded["id"]


@app.route("/")
def home():
    return "⚡ Flask Render + Google Drive API đang chạy OK!"


@app.route("/upload-test")
def upload_test():
    df = pd.DataFrame({
        "Time": ["10:00", "10:05", "10:10"],
        "Power (kW)": [12, 14, 15]
    })

    file_name = "test_upload.xlsx"
    df.to_excel(file_name, index=False)

    file_id = upload_excel_to_drive(file_name, file_name)
    return f"✔ Upload thành công!<br>File ID: {file_id}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
