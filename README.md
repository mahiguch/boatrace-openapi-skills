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

詳細は [skills/boatrace-openapi/SKILL.md](skills/boatrace-openapi/SKILL.md) を参照してください。

## インストール方法

### Claude Code での利用

Claude CodeでSKILL.mdファイルを開くと、スキルが自動的にインストールされます。

#### 方法1: URLからインストール（推奨）

GitHubリポジトリのURLを使用してインストール：

1. Claude Code を開く
2. 左のパネルで **Skills** タブをクリック
3. **+ Add skill** をクリック
4. **From URL** を選択
5. 以下のURLを入力：
   ```
   https://github.com/mahiguch/boatrace-openapi-skills/tree/main/skills/boatrace-openapi
   ```
6. **Install** をクリック

#### 方法2: SKILL.mdファイルから直接インストール

1. [skills/boatrace-openapi/SKILL.md](skills/boatrace-openapi/SKILL.md) をClaudeに送信
2. Claude Code がスキルを自動的に認識
3. スキルをインストール

#### 方法3: 手動で .skill ファイルをインポート

1. スキルをパッケージング：
   ```bash
   python3 tools/scripts/package_skill.py skills/boatrace-openapi ./dist
   ```
2. 生成された `.skill` ファイルを Claude Code にドラッグ＆ドロップ

### スキル内容の確認

インストール後、スキルの説明や使用方法は以下で確認できます：

- **スキル説明**: [SKILL.md](skills/boatrace-openapi/SKILL.md)
- **API仕様**: [api_specification.md](skills/boatrace-openapi/references/api_specification.md)
- **競艇場番号一覧**: [SKILL.md の競艇場番号の対応表](skills/boatrace-openapi/SKILL.md#競艇場番号の対応表)

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
