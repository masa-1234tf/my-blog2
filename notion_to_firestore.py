import requests
import json
# Notion API 設定
NOTION_API_KEY = "secret_o3d9jwkOFkjKbKhmtuXlU33WFb4iQDJdffqU4au8dyY"  # Notion APIキー
DATABASE_ID = "3b765b970c9e4365acb475dbb9fa7d9c"  # Notion データベースID

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