from flask import Flask
import os
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Path to secret file mounted by Render
CREDS_PATH = "/etc/secrets/creds.json"

# Google Drive Folder ID from Render environment variables
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
    return "⚡ Flask đang chạy trên Render – API Google Drive OK"


@app.route("/upload-test")
def upload_test():
    df = pd.DataFrame({
        "Time": ["10:00", "10:05", "10:10"],
        "Power (kW)": [12, 14, 15]
    })

    file_name = "test_upload.xlsx"
    df.to_excel(file_name, index=False)

    file_id = upload_excel_to_drive(file_name, file_name)

    return f"Đã upload test_upload.xlsx ✔<br>File ID Google Drive: {file_id}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
