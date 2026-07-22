import argparse
import logging

from io_utils import load_subscribers, load_cdrs, write_report
from rating import compute_cost
from fraud import is_suspicious
from reporting import build_report


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    parser = argparse.ArgumentParser(
        description="Telecom CDR Billing Insights CLI"
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

    subscribers = load_subscribers(args.subscribers)
    cdrs = load_cdrs(args.cdrs)

    suspicious_calls = []
    unknown_subscribers = set()

    for cdr in cdrs:

        cdr.cost = compute_cost(cdr)

        if cdr.msisdn in subscribers:

            subscribers[cdr.msisdn].add_call(cdr)

            if is_suspicious(cdr):
                suspicious_calls.append(cdr)

        else:
            unknown_subscribers.add(cdr.msisdn)

    report = build_report(
        subscribers,
        suspicious_calls,
        unknown_subscribers
    )

    write_report(report, args.output)

    print("\n===== Processing Summary =====")
    print(f"Subscribers Loaded : {len(subscribers)}")
    print(f"CDRs Processed     : {len(cdrs)}")
    print(f"Unknown Numbers    : {len(unknown_subscribers)}")
    print(f"Suspicious Calls   : {len(suspicious_calls)}")
    print(f"Report Written To  : {args.output}")


if __name__ == "__main__":
    main()