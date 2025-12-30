#!/usr/bin/env python3
"""
Boatrace Open API Data Fetcher

Fetches programs, results, and preview data from Boatrace Open API.
"""

import argparse
import json
import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# Constants for validation
VALID_STADIUM_RANGE = (1, 24)
VALID_RACE_RANGE = (1, 12)


def filter_races(
    data: dict,
    endpoint: str,
    race_stadium_number: int | None,
    race_number: int | None
) -> dict:
    """
    Filter race data by stadium number and/or race number.

    Args:
        data: API response data
        endpoint: Endpoint name (determines the key name: 'programs', 'results', or 'previews')
        race_stadium_number: Stadium number to filter (1-24), or None for no filtering
        race_number: Race number to filter (1-12), or None for no filtering

    Returns:
        dict: Filtered data with the same structure as input
    """
    # Error responses should pass through unchanged
    if "error" in data:
        return data

    # Get the appropriate key based on endpoint
    key = endpoint  # 'programs', 'results', or 'previews'

    if key not in data:
        return data

    races = data[key]

    # Apply filters
    filtered_races = races

    if race_stadium_number is not None:
        filtered_races = [
            race for race in filtered_races
            if race.get("race_stadium_number") == race_stadium_number
        ]

    if race_number is not None:
        filtered_races = [
            race for race in filtered_races
            if race.get("race_number") == race_number
        ]

    # Return filtered data with the same structure
    return {key: filtered_races}


def fetch_data(
    endpoint: str,
    yyyy: str,
    yyyymmdd: str,
    race_stadium_number: int | None = None,
    race_number: int | None = None
) -> dict:
    """
    Fetch data from Boatrace Open API.

    Args:
        endpoint: One of 'programs', 'results', or 'previews'
        yyyy: Year (e.g., '2025')
        yyyymmdd: Date in YYYYMMDD format (e.g., '20251222')
        race_stadium_number: Filter by race stadium number (1-24), optional
        race_number: Filter by race number (1-12), optional

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

    # Validate filter parameters
    if race_stadium_number is not None:
        if not isinstance(race_stadium_number, int) or not (VALID_STADIUM_RANGE[0] <= race_stadium_number <= VALID_STADIUM_RANGE[1]):
            return {
                "error": {
                    "type": "INVALID_PARAMETERS",
                    "message": "race_stadium_number must be an integer between 1 and 24",
                    "details": {
                        "race_stadium_number": race_stadium_number
                    }
                }
            }

    if race_number is not None:
        if not isinstance(race_number, int) or not (VALID_RACE_RANGE[0] <= race_number <= VALID_RACE_RANGE[1]):
            return {
                "error": {
                    "type": "INVALID_PARAMETERS",
                    "message": "race_number must be an integer between 1 and 12",
                    "details": {
                        "race_number": race_number
                    }
                }
            }

    # Build URL
    url = f"https://boatraceopenapi.github.io/{endpoint}/v2/{yyyy}/{yyyymmdd}.json"

    try:
        # Fetch data
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            # Apply filters if specified
            filtered_data = filter_races(data, endpoint, race_stadium_number, race_number)
            return filtered_data

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
    parser = argparse.ArgumentParser(
        description="Fetch boatrace data from Boatrace Open API"
    )
    parser.add_argument(
        "endpoint",
        choices=["programs", "results", "previews"],
        help="Endpoint type"
    )
    parser.add_argument(
        "yyyy",
        help="Year (e.g., 2025)"
    )
    parser.add_argument(
        "yyyymmdd",
        help="Date in YYYYMMDD format (e.g., 20251222)"
    )
    parser.add_argument(
        "--stadium",
        type=int,
        default=None,
        help="Filter by race stadium number (1-24)"
    )
    parser.add_argument(
        "--race",
        type=int,
        default=None,
        help="Filter by race number (1-12)"
    )

    args = parser.parse_args()

    result = fetch_data(
        args.endpoint,
        args.yyyy,
        args.yyyymmdd,
        race_stadium_number=args.stadium,
        race_number=args.race
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
