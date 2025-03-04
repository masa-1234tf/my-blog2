# 🔗 API設計書

## 1️⃣ 概要
- **エンドポイント:** `/api/articles`
- **認証:** `不要`（記事一覧は公開API）
- **レスポンス形式:** `JSON`
- **主な機能:** 記事一覧取得

---

## 2️⃣ エンドポイント一覧

フィールド	型	説明
title	title	記事タイトル
description	rich_text	記事の説明
date	date	記事の日付
category	multi_select	カテゴリー（複数選択可能）
tag	multi_select	タグ（複数選択可能）
published	checkbox	公開フラグ（true / false）
thumbnail	files	記事のサムネイル画像
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
