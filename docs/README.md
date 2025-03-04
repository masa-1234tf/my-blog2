# MyBlog2 - ブログプロジェクト

## 📌 プロジェクト概要
以前作ったNUxt.js + NotionのブログはNotionから直接APIで表示していたためページ表示速度が遅く改良をします。
Nuxt.js + Firebase で作るブログ。Notion API から記事を取得し、Firestore に保存してフロントで表示。

## 🚀 使用技術
- フロントエンド: Nuxt.js, TypeScript
- バックエンド: Firebase Functions, Firestore, Cloudflare R2
- インフラ: Vercel, GitHub Actions
- API: Notion API, Firestore API

## ✅ 機能一覧
- 記事一覧・詳細表示
- タグ & カテゴリー管理
- 記事検索
- APIを通じた記事の自動取得

## 📂 ドキュメント一覧
- [フローチャート設計](docs/flowchart.png)
- [サイトマップ](docs/sitemap.md)
- [API設計](docs/api.md)
- [ER図（データベース設計）](docs/er-diagram.png)
- [ファイル構成](docs/file_structure.md)
