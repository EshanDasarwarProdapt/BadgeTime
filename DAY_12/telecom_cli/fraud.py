from models import CallDataRecord
from config import DEFAULT_FRAUD_THRESHOLD


def is_suspicious(call_record: CallDataRecord, threshold=DEFAULT_FRAUD_THRESHOLD) -> bool:
    """
    Determines if a call record is suspicious based on its duration and cost.

    Args:
        call_record (CallDataRecord): The call record to evaluate.
        threshold (int): Duration threshold in seconds for international calls.

    Returns:
        bool: True if the call is suspicious, False otherwise.
    """
    return call_record.is_suspicious(threshold)

