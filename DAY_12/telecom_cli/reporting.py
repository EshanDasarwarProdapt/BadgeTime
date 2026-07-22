from typing import Dict, List, Set

from models import Subscriber, CallDataRecord


def build_report(
    subscribers: Dict[str, Subscriber],
    suspicious_calls: List[CallDataRecord],
    unknown_subscribers: Set[str]
) -> dict:
    """
    Builds the final report.

    Args:
        subscribers (Dict[str, Subscriber]): Subscriber dictionary.
        suspicious_calls (List[CallDataRecord]): List of suspicious CDRs.
        unknown_subscribers (Set[str]): Set of unknown subscriber MSISDNs.

    Returns:
        dict: Report dictionary.
    """

    report = {
        "subscribers": {},
        "suspicious_calls": [],
        "unknown_subscribers": list(unknown_subscribers)
    }

    for msisdn, subscriber in subscribers.items():
        report["subscribers"][msisdn] = {
            "plan_type": subscriber.plan_type,
            "call_count": len(subscriber.calls),
            "total_cost": subscriber.total_cost()
        }

    for cdr in suspicious_calls:
        report["suspicious_calls"].append({
            "msisdn": cdr.msisdn,
            "call_type": cdr.call_type,
            "duration_sec": cdr.duration_sec,
            "cost": cdr.cost
        })

    return report