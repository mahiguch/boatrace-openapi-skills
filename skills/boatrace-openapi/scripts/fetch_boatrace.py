#!/usr/bin/env python3
"""
Boatrace Open API Data Fetcher

Fetches programs, results, and preview data from Boatrace Open API.
"""

import json
import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def fetch_data(endpoint: str, yyyy: str, yyyymmdd: str) -> dict:
    """
    Fetch data from Boatrace Open API.

    Args:
        endpoint: One of 'programs', 'results', or 'previews'
        yyyy: Year (e.g., '2025')
        yyyymmdd: Date in YYYYMMDD format (e.g., '20251222')

    Returns:
        dict: API response or error object
    """

    # Validate inputs
    if endpoint not in ['programs', 'results', 'previews']:
        return {
            "error": {
                "type": "INVALID_PARAMETERS",
                "message": "endpoint must be one of: programs, results, previews",
                "details": {
                    "endpoint": endpoint
                }
            }
        }

    if not yyyy or len(yyyy) != 4 or not yyyy.isdigit():
        return {
            "error": {
                "type": "INVALID_PARAMETERS",
                "message": "yyyy must be a 4-digit year",
                "details": {
                    "yyyy": yyyy
                }
            }
        }

    if not yyyymmdd or len(yyyymmdd) != 8 or not yyyymmdd.isdigit():
        return {
            "error": {
                "type": "INVALID_PARAMETERS",
                "message": "yyyymmdd must be in YYYYMMDD format",
                "details": {
                    "yyyymmdd": yyyymmdd
                }
            }
        }

    # Build URL
    url = f"https://boatraceopenapi.github.io/{endpoint}/v2/{yyyy}/{yyyymmdd}.json"

    try:
        # Fetch data
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data

    except HTTPError as e:
        if e.code == 404:
            return {
                "error": {
                    "type": "NOT_FOUND",
                    "message": f"Data not found for date {yyyymmdd}",
                    "details": {
                        "url": url,
                        "status": 404
                    }
                }
            }
        else:
            return {
                "error": {
                    "type": "API_ERROR",
                    "message": f"API returned HTTP {e.code}",
                    "details": {
                        "url": url,
                        "status": e.code
                    }
                }
            }

    except (URLError, TimeoutError) as e:
        return {
            "error": {
                "type": "NETWORK_ERROR",
                "message": "Failed to connect to the API",
                "details": {
                    "url": url,
                    "status": str(e)
                }
            }
        }

    except json.JSONDecodeError as e:
        return {
            "error": {
                "type": "API_ERROR",
                "message": "Invalid JSON response from API",
                "details": {
                    "url": url,
                    "status": str(e)
                }
            }
        }

    except Exception as e:
        return {
            "error": {
                "type": "API_ERROR",
                "message": f"Unexpected error: {str(e)}",
                "details": {
                    "url": url,
                    "status": str(e)
                }
            }
        }


def main():
    """Command line interface for fetching Boatrace data."""

    if len(sys.argv) < 4:
        print("Usage: python fetch_boatrace.py <endpoint> <yyyy> <yyyymmdd>")
        print("  endpoint: programs, results, or previews")
        print("  yyyy: Year (e.g., 2025)")
        print("  yyyymmdd: Date in YYYYMMDD format (e.g., 20251222)")
        sys.exit(1)

    endpoint = sys.argv[1]
    yyyy = sys.argv[2]
    yyyymmdd = sys.argv[3]

    result = fetch_data(endpoint, yyyy, yyyymmdd)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
