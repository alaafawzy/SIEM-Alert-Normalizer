from .base import BaseNormalizer
from datetime import datetime

class QRadarNormalizer(BaseNormalizer):
    source_type = "qradar"

    def normalize(self):
        raw = self.raw_data

        # Severity mapping (you can fine-tune this)
        alert_severity= self.map_severity(raw["severity"])

        return {
            "source_type": self.source_type,
            "rule": ", ".join(rule.get("name", "") for rule in raw.get("rules", [])) or "Unknown Rule",
            "alert_severity": alert_severity,
            "reason": raw.get("description", "N/A"),
            "source_ip": raw.get("offense_source", ""),
            "status": self.map_status(raw.get("status","")),
            "start_time": raw.get("start_time"),
            "offense_type": raw.get("offense_type", ""),
            "magnitude": raw.get("magnitude",""),
            "credibility": raw.get("credibility",""),
            "relevance":raw.get("relevance", ""),
            "categories": raw.get("categories",""),
            "source_address_ids": raw.get("source_address_ids", ""),
            "destination_address_ids": raw.get("destination_address_ids", "")
        }


    def map_severity(self, numeric_severity):
        if numeric_severity >= 8:
            return "Critical"
        elif numeric_severity >= 6:
            return "High"
        elif numeric_severity >= 4:
            return "Medium"
        else:
            return "Low"

    def map_status(self, qradar_status):
        if qradar_status == "OPEN":
            return "reported"
        elif qradar_status == "CLOSED":
            return "remediated"
        else:
            return "reported"