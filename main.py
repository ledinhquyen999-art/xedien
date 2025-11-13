from flask import Flask
import os
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Secret file path (Render sẽ mount tại /etc/secrets/creds.json)
CREDS_PATH = "/etc/secrets/creds.json"
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
    return "🚀 Flask Render + Google Drive API đang chạy OK!"

@app.route("/upload-test")
def upload_test():
    df = pd.DataFrame({
        "Time": ["10:00", "10:05", "10:10"],
        "Power (kW)": [12, 14, 15]
    })

    file_name = "test_upload.xlsx"
    df.to_excel(file_name, index=False

