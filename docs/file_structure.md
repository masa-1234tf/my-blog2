myblog2/
├── backend/                   # FastAPI バックエンド
│   ├── app/                   # FastAPI アプリ本体
│   │   ├── [main.py](http://main.py/)            # エントリーポイント（APIエンドポイント定義）
│   │   ├── routes/            # 各APIルートの処理
│   │   │   ├── [notion.py](http://notion.py/)      # Notion API からデータ取得
│   │   │   ├── [articles.py](http://articles.py/)    # 記事関連のAPI
│   │   │   ├── [storage.py](http://storage.py/)     # 画像のアップロード処理
│   │   ├── models/            # データモデル（Firestore用）
│   │   │   ├── [article.py](http://article.py/)     # 記事のデータ構造
│   │   ├── services/          # 外部APIとの連携
│   │   │   ├── [firestore.py](http://firestore.py/)   # Firestore 操作
│   │   │   ├── cloud_storage.py # Cloud Storage 操作
│   │   ├── utils/             # 共通関数
│   │   │   ├── [config.py](http://config.py/)      # 設定ファイル（環境変数読み込み）
│   │   │   ├── [logger.py](http://logger.py/)      # ロギング機能
│   ├── .env                   # 環境変数（Git管理しない）
│   ├── requirements.txt       # 必要なパッケージ一覧
│   ├── Dockerfile             # Docker設定（デプロイ用）
│   ├── [README.md](http://readme.md/)              # バックエンドの概要
│   ├── tests/                 # APIテスト
│   │   ├── test_articles.py   # 記事APIのテスト
│   │   ├── test_notion.py     # Notion APIテスト
│   ├── [uvicorn.sh](http://uvicorn.sh/)             # FastAPIの起動スクリプト
│   ├── .gitignore             # Git管理対象外のファイル
│   ├── [gunicorn.conf.py](http://gunicorn.conf.py/)       # Gunicorn設定（本番用）
│   ├── [startup.sh](http://startup.sh/)             # 本番用の起動スクリプト
│   ├── alembic/               # データベースマイグレーション管理
│   ├── migrations/            # Firestoreのデータ移行スクリプト
│   ├── docs/                  # APIドキュメント（Swagger, Redoc用）
│   ├── nginx/                 # Nginxリバースプロキシ設定
│   ├── docker-compose.yml     # Dockerコンテナ管理
│   ├── Makefile               # 簡単な開発タスク管理
│   ├── pyproject.toml         # Pythonプロジェクトの設定
│   ├── poetry.lock            # Poetry（Pythonパッケージ管理）用
│   ├── dev-requirements.txt   # 開発環境のパッケージ
│   ├── prod-requirements.txt  # 本番環境のパッケージ
│   ├── [entrypoint.sh](http://entrypoint.sh/)          # Docker起動時のスクリプト
│   ├── logs/                  # ログ管理
│   ├── crontab/               # 定期実行ジョブ設定
│   ├── bin/                   # 実行スクリプト
│   ├── backups/               # Firestoreのバックアップデータ
│   ├── scripts/               # 開発・データ移行スクリプト
│   │   ├── fetch_notion.py    # Notion APIからデータ取得
│   │   ├── backup_firestore.py # Firestoreデータのバックアップ
│   │   ├── upload_images.py   # 画像をCloud Storageにアップロード
│   ├── testdata/              # テスト用データ

├── frontend/                  # Nuxt.js フロントエンド
│   ├── components/            # Vueコンポーネント
│   │   ├── ArticleList.vue    # 記事一覧コンポーネント
│   │   ├── ArticleCard.vue    # 記事カードコンポーネント
│   │   ├── ArticleDetail.vue  # 記事詳細コンポーネント
│   ├── pages/                 # ルーティング用ページ
│   │   ├── index.vue          # トップページ
│   │   ├── articles.vue       # 記事一覧ページ
│   │   ├── articles/[id].vue  # 記事詳細ページ
│   │   ├── about.vue          # サイト概要
│   │   ├── search.vue         # 検索ページ
│   ├── layouts/               # レイアウト
│   │   ├── default.vue        # メインレイアウト
│   ├── store/                 # Vuex / Pinia ストア
│   ├── plugins/               # プラグイン
│   ├── assets/                # 画像・CSS・フォント
│   ├── static/                # 静的ファイル
│   ├── middleware/            # ミドルウェア（認証など）
│   ├── composables/           # Vue3のComposition API用
│   ├── nuxt.config.ts         # Nuxtの設定
│   ├── tsconfig.json          # TypeScript設定
│   ├── .env                   # 環境変数
│   ├── package.json           # フロントエンドの依存関係
│   ├── yarn.lock              # 依存関係のロックファイル
│   ├── [README.md](http://readme.md/)              # フロントエンドの概要

├── deploy/                    # デプロイ用スクリプト
│   ├── [deploy.sh](http://deploy.sh/)              # デプロイ用のシェルスクリプト
│   ├── firebase.json          # Firebaseホスティング設定
│   ├── netlify.toml           # Netlify設定

├── .gitignore                 # Git管理対象外のファイル
├── [README.md](http://readme.md/)                  # プロジェクトの概要