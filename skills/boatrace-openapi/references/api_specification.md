# Boatrace Open API Specification

## Overview

Boatrace Open APIは、ボートレースの出走表、結果、直前情報をJSON形式で提供するOpen APIです。

## Endpoints

### Programs (出走表)
- **URL**: `https://boatraceopenapi.github.io/programs/v2/{YYYY}/{YYYYMMDD}.json`
- **説明**: 指定日のレース出走表データを取得
- **パラメータ**:
  - `YYYY`: 年 (例: 2025)
  - `YYYYMMDD`: 年月日 (例: 20251222)

### Results (結果)
- **URL**: `https://boatraceopenapi.github.io/results/v2/{YYYY}/{YYYYMMDD}.json`
- **説明**: 指定日のレース結果データを取得
- **パラメータ**:
  - `YYYY`: 年 (例: 2025)
  - `YYYYMMDD`: 年月日 (例: 20251222)

### Previews (直前情報)
- **URL**: `https://boatraceopenapi.github.io/previews/v2/{YYYY}/{YYYYMMDD}.json`
- **説明**: 指定日のレース直前情報（選手情報など）を取得
- **パラメータ**:
  - `YYYY`: 年 (例: 2025)
  - `YYYYMMDD`: 年月日 (例: 20251222)

## Response Format

すべてのエンドポイントはJSON形式でレスポンスを返します。

## Filtering (クライアント側実装)

fetch_boatrace.py スクリプトでは、APIから取得したデータをクライアント側でフィルタリングできます。これによりトークン使用量を削減できます。

### フィルタパラメータ

- **race_stadium_number**: 競艇場番号 (1-24) でフィルタリング
- **race_number**: レース番号 (1-12) でフィルタリング

### フィルタリング動作

- 両パラメータは独立して指定可能
- 両方指定した場合、AND 条件で絞り込まれます
- フィルタに一致するレースが0件の場合、空配列が返されます
- エラーレスポンスはそのまま返されます

### 使用例

```bash
# 競艇場2のすべてのレース（12件）を取得
python fetch_boatrace.py programs 2025 20251222 --stadium 2

# すべての競艇場のレース3（複数スタジアム）を取得
python fetch_boatrace.py programs 2025 20251222 --race 3

# 競艇場2のレース3のみを取得（AND条件）
python fetch_boatrace.py programs 2025 20251222 --stadium 2 --race 3
```

## Error Handling

APIが利用できない場合や、指定した日付のデータが存在しない場合は、以下のエラー形式で返します：

```json
{
  "error": {
    "type": "ERROR_TYPE",
    "message": "Error description",
    "details": {
      "url": "requested url",
      "status": "http status code or error reason"
    }
  }
}
```

エラータイプ：
- `NOT_FOUND`: データが見つからない (404)
- `NETWORK_ERROR`: ネットワークエラー
- `INVALID_PARAMETERS`: パラメータが無効（フィルタパラメータの範囲外を含む）
- `API_ERROR`: API側のエラー
