# Boatrace Skills

ボートレースのデータを取得・処理するためのClaudeスキル集です。

## Skills

### boatrace-openapi

Boatrace Open APIから以下のデータを取得します：

- **programs** (出走表): レースの出走表データ
- **results** (結果): レース結果データ
- **previews** (直前情報): 選手情報などの直前情報

**使用方法:**
```bash
python skills/boatrace-openapi/scripts/fetch_boatrace.py programs 2025 20251222
python skills/boatrace-openapi/scripts/fetch_boatrace.py results 2025 20251222
python skills/boatrace-openapi/scripts/fetch_boatrace.py previews 2025 20251222
```

## ファイル構成

```
boatrace-skills/
├── README.md                          # このファイル
├── .gitignore                         # Git除外設定
├── .github/
│   └── workflows/
│       └── package-skills.yml        # スキルのパッケージング自動化
├── skills/
│   └── boatrace-openapi/             # スキルのソースコード
│       ├── SKILL.md                  # スキルの説明
│       ├── scripts/
│       │   └── fetch_boatrace.py     # APIデータ取得スクリプト
│       └── references/
│           ├── api_specification.md  # API仕様書
│           └── api_reference.md      # API参考資料
└── tools/
    └── scripts/                       # スキルパッケージング用ツール
```

## スキルの開発

### 新しいスキルを追加する場合

1. `skills/` ディレクトリに新しいスキルディレクトリを作成
2. `SKILL.md`、`scripts/`、`references/` を配置
3. Gitにコミット＆プッシュ
4. GitHub Actionsが自動的に`.skill`ファイルをパッケージング

### スキルの構成

各スキルは以下の構成を持つ必要があります：

```
skill-name/
├── SKILL.md              # メタデータと説明（必須）
├── scripts/              # 実行可能なPythonスクリプト（必要に応じて）
└── references/           # ドキュメント・参考資料（必要に応じて）
```

## パッケージング

スキルは自動的にGitHub Actions経由でパッケージングされます。

手動でパッケージングする場合：

```bash
python3 tools/scripts/package_skill.py skills/boatrace-openapi ./dist
```

## ライセンス

未決定
