---
name: boatrace-openapi
description: Fetch boatrace data from Boatrace Open API. Retrieve program schedules, race results, and preview information by specifying year and date. Use when you need to access boatrace race information, programs (出走表), results, or preview data (直前情報) for a specific date.
---

# Boatrace Open API

Boatrace Open APIスキルは、ボートレースの出走表、結果、直前情報をJSON形式で取得するためのツールです。指定した年月日のレース情報を簡単に取得できます。

## Quick Start

3つのエンドポイントがあります：

```bash
# 出走表を取得
python scripts/fetch_boatrace.py programs 2025 20251222

# レース結果を取得
python scripts/fetch_boatrace.py results 2025 20251222

# 直前情報を取得
python scripts/fetch_boatrace.py previews 2025 20251222
```

## Parameters

- **endpoint**: `programs` (出走表), `results` (結果), または `previews` (直前情報)
- **YYYY**: 年 (例: 2025)
- **YYYYMMDD**: 年月日 (例: 20251222)

## Error Handling

スクリプトは標準化されたエラー形式を使用します：

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
- `INVALID_PARAMETERS`: パラメータが無効
- `NOT_FOUND`: データが見つからない (404)
- `NETWORK_ERROR`: ネットワークエラー
- `API_ERROR`: API側のエラー

## Resources

### scripts/
- `fetch_boatrace.py`: Boatrace Open APIからデータを取得するPythonスクリプト

### references/
- `api_specification.md`: API仕様の詳細情報
