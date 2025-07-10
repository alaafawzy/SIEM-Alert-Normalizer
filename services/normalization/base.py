import abc

class BaseNormalizer(abc.ABC):
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def map_severity(self, severity):
        return {
            "Low": "Low",
            "Medium": "Medium",
            "High": "High",
            "Critical": "Critical",
            "1": "Low",
            "2": "Medium",
            "3": "High",
            "4": "Critical"
        }.get(str(severity).capitalize(), "Unknown")

    def map_status(self, status):
        return {
            "Open": "Open",
            "Closed": "Closed",
            "New": "Open",
            "Resolved": "Closed"
        }.get(str(status).capitalize(), "Unknown")

    @abc.abstractmethod
    def normalize(self):
        """Normalize raw alert"""
        pass
