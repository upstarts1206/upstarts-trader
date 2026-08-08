class MarketEvent:

    def __init__(self, event_type, timestamp, price, metadata=None):

        self.event_type = event_type
        self.timestamp = timestamp
        self.price = price
        self.metadata = metadata or {}

    def __repr__(self):

        return (
            f"{self.event_type} | "
            f"{self.timestamp} | "
            f"{self.price}"
        )