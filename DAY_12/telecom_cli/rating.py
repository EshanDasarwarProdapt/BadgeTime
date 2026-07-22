from models import CallDataRecord
from config import RATES


def compute_cost(call_record: CallDataRecord) -> float:
    """
    Computes the cost of a call based on its type and duration.

    Args:
        call_record (CallDataRecord): The call record.

    Returns:
        float: Cost of the call rounded to 2 decimal places.
    """
    rate = RATES.get(call_record.call_type, RATES["domestic"])

    duration_minutes = call_record.duration_sec / 60

    cost = duration_minutes * rate

    return round(cost, 2)