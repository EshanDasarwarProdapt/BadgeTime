import csv
import json
import logging

from models import Subscriber, CallDataRecord



def load_subscribers(json_path: str) -> dict:
    """
    Loads subscribers from a JSON file.

    Args:
        json_path (str): Path to the subscribers JSON file.

    Returns:
        dict: Dictionary of Subscriber objects keyed by MSISDN.
    """
    subscribers = {}

    with open(json_path, "r") as file:
        data = json.load(file)

        for subscriber in data:
            msisdn = subscriber["msisdn"]
            plan_type = subscriber["plan_type"]

            subscribers[msisdn] = Subscriber(msisdn, plan_type)

    return subscribers

def parse_cdr_line(row: dict) -> dict:
    """
    Parses and validates a single CDR row.

    Args:
        row (dict): A row read from csv.DictReader.

    Returns:
        dict: Parsed CDR data.

    Raises:
        ValueError: If any required field is missing or invalid.
    """
    try:
        msisdn = row["msisdn"].strip()
        call_type = row["call_type"].strip().lower()
        duration_sec = int(row["duration_sec"])

        if call_type not in ("domestic", "roaming", "international"):
            raise ValueError(f"Invalid call type: {call_type}")

        if duration_sec < 0:
            raise ValueError("Duration cannot be negative")

        return {
            "msisdn": msisdn,
            "call_type": call_type,
            "duration_sec": duration_sec
        }

    except (KeyError, ValueError) as e:
        raise ValueError(f"Malformed CDR row: {row}") from e


def load_cdrs(csv_path: str) -> list:
    """
    Loads Call Detail Records from a CSV file.

    Args:
        csv_path (str): Path to the CDR CSV file.

    Returns:
        list: List of valid CallDataRecord objects.
    """
    cdrs = []

    with open(csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                parsed_row = parse_cdr_line(row)

                cdr = CallDataRecord(
                    parsed_row["msisdn"],
                    parsed_row["call_type"],
                    parsed_row["duration_sec"]
                )

                cdrs.append(cdr)

            except ValueError as e:
                logging.error(f"Skipping malformed row: {e}")

    return cdrs


def write_report(report: dict, output_path: str) -> None:
    """
    Writes the report to a JSON file.

    Args:
        report (dict): Report dictionary.
        output_path (str): Output JSON file path.
    """
    with open(output_path, "w") as file:
        json.dump(report, file, indent=4)