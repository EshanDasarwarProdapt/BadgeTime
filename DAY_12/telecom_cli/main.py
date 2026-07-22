import argparse
import logging

from io_utils import load_subscribers, load_cdrs, write_report
from rating import compute_cost
from fraud import is_suspicious
from reporting import build_report


def setup_logging() -> None:
    """
    Configures logging for the Telecom Billing CLI.
    """
    logging.basicConfig(
        filename="telecom.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w"
    )


def main():

    setup_logging()

    logging.info("Telecom Billing CLI Started.")

    parser = argparse.ArgumentParser(
        description="Telecom Billing Insights CLI"
    )

    parser.add_argument(
        "--subscribers",
        required=True,
        help="Path to subscribers JSON file"
    )

    parser.add_argument(
        "--cdrs",
        required=True,
        help="Path to CDR CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output report JSON file"
    )

    args = parser.parse_args()

    # Load subscribers
    subscribers = load_subscribers(args.subscribers)
    logging.info(f"Loaded {len(subscribers)} subscribers.")

    # Load CDRs
    cdrs = load_cdrs(args.cdrs)
    logging.info(f"Loaded {len(cdrs)} valid CDRs.")

    suspicious_calls = []
    unknown_subscribers = set()

    # Process every CDR
    for cdr in cdrs:

        # Compute call cost
        cdr.cost = compute_cost(cdr)

        # Check if subscriber exists
        if cdr.msisdn in subscribers:

            subscriber = subscribers[cdr.msisdn]

            subscriber.add_call(cdr)

            if is_suspicious(cdr):
                suspicious_calls.append(cdr)
                logging.warning(
                    f"Suspicious call detected: {cdr.msisdn}"
                )

        else:
            unknown_subscribers.add(cdr.msisdn)
            logging.warning(
                f"Unknown subscriber: {cdr.msisdn}"
            )

    # Build report
    report = build_report(
        subscribers,
        suspicious_calls,
        unknown_subscribers
    )

    # Write report
    write_report(report, args.output)

    logging.info(f"Report written to {args.output}")

    print("\n========== Processing Summary ==========")
    print(f"Subscribers Loaded : {len(subscribers)}")
    print(f"CDRs Processed     : {len(cdrs)}")
    print(f"Suspicious Calls   : {len(suspicious_calls)}")
    print(f"Unknown Numbers    : {len(unknown_subscribers)}")
    print(f"Output Report      : {args.output}")
    print("Log File           : telecom.log")
    print("========================================")

    logging.info("Telecom Billing CLI Completed Successfully.")


if __name__ == "__main__":
    main()