# 🔗 API設計書

## 1️⃣ 概要
- **エンドポイント:** `/api/articles`
- **認証:** `不要`（記事一覧は公開API）
- **レスポンス形式:** `JSON`
- **主な機能:** 記事一覧取得

---

## 2️⃣ エンドポイント一覧

| メソッド | エンドポイント | 説明 | 認証 |
|----------|--------------|------|------|
| `GET`  | `/api/articles` | 記事一覧を取得 | なし |
| `GET`  | `/api/articles/{id}` | 記事詳細を取得 | なし |
| `POST` | `/api/articles` | 記事を作成（管理者のみ） | 必要 |
| `DELETE` | `/api/articles/{id}` | 記事を削除（管理者のみ） | 必要 |

---

## 3️⃣ API詳細設計

### **① 記事一覧取得**
- **エンドポイント:** `GET /api/articles`
- **認証:** `不要`
- **レスポンス（JSON）**
```json
{
  "articles": [
    {
      "id": "abc123",
      "title": "Nuxt.jsとFirebaseでブログを作る",
      "date": "2024-07-20",
      "category": "プログラミング",
      "tags": ["Nuxt", "Firebase"],
      "thumbnail": "https://r2.cloudflare.com/articles/abc123/thumbnail.jpg",
      "published": true
    }
  ]
}
