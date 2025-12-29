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
- `INVALID_PARAMETERS`: パラメータが無効
- `API_ERROR`: API側のエラー
