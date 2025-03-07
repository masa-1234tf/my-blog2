import requests
import json
import os
from dotenv import load_dotenv

# .env を読み込む
load_dotenv()
# Notion API 設定
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

# 🔹 Notion API から記事データを取得
def fetch_notion_data():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)


    return response.json()
notion_data = fetch_notion_data()

# JSON全体を見やすく表示
import json
print(json.dumps(notion_data, indent=4, ensure_ascii=False))  # 日本語対応