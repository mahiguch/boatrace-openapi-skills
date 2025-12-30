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

### フィルタリング

特定の競艇場やレース番号で絞り込むことができます：

```bash
# 競艇場2（戸田）のみを取得
python scripts/fetch_boatrace.py programs 2025 20251222 --stadium 2

# レース3のみを取得（全競艇場）
python scripts/fetch_boatrace.py programs 2025 20251222 --race 3

# 競艇場4（平和島）のレース10のみを取得
python scripts/fetch_boatrace.py programs 2025 20251222 --stadium 4 --race 10
```

## 競艇場番号の対応表

`--stadium` パラメータで以下の番号を使用します：

| 番号 | 競艇場 | 番号 | 競艇場 | 番号 | 競艇場 | 番号 | 競艇場 |
|-----|--------|-----|--------|-----|--------|-----|--------|
| 1 | 桐生 | 7 | 蒲郡 | 13 | 尼崎 | 19 | 下関 |
| 2 | 戸田 | 8 | 常滑 | 14 | 鳴門 | 20 | 若松 |
| 3 | 江戸川 | 9 | 津 | 15 | 丸亀 | 21 | 芦屋 |
| 4 | 平和島 | 10 | 三国 | 16 | 児島 | 22 | 福岡 |
| 5 | 多摩川 | 11 | びわこ | 17 | 宮島 | 23 | 唐津 |
| 6 | 浜名湖 | 12 | 住之江 | 18 | 徳山 | 24 | 大村 |

### 使用例

**会話例**：「今日の平和島第10レースの番組表を取得したい」

```bash
# 平和島 = 番号4、レース = 10
python scripts/fetch_boatrace.py programs 2025 20251222 --stadium 4 --race 10
```

## Parameters

- **endpoint**: `programs` (出走表), `results` (結果), または `previews` (直前情報)
- **YYYY**: 年 (例: 2025)
- **YYYYMMDD**: 年月日 (例: 20251222)
- **--stadium**: フィルタ対象の競艇場番号 (1-24、オプション)。[競艇場番号の対応表](#競艇場番号の対応表)を参照
- **--race**: フィルタ対象のレース番号 (1-12、オプション)

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
