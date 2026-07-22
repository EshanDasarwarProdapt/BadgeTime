class Subscriber:
    """
    Represents a telecom subscriber.
    """

    def __init__(self, msisdn, plan_type):
        self.msisdn = msisdn
        self.plan_type = plan_type
        self.calls = []

    def add_call(self, cdr):
        self.calls.append(cdr)

    def total_cost(self):
        total = 0
        for call in self.calls:
            total += call.cost
        return round(total, 2)

    def __str__(self):
        return (f"Subscriber(msisdn={self.msisdn}, "
                f"plan_type={self.plan_type})")


class CallDataRecord:
    """
    Represents a single Call Detail Record (CDR).
    """

    def __init__(self, msisdn, call_type, duration_sec):
        self.msisdn = msisdn
        self.call_type = call_type
        self.duration_sec = duration_sec
        self.cost = 0.0

    def is_suspicious(self, threshold=3600):
        if self.duration_sec > 0 and self.cost == 0:
            return True

        if self.call_type == "international" and self.duration_sec > threshold:
            return True

        return False

    def __str__(self):
        return (f"CallDataRecord(msisdn={self.msisdn}, "
                f"call_type={self.call_type}, "
                f"duration_sec={self.duration_sec}, "
                f"cost={self.cost})")