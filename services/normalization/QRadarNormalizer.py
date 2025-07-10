from services.normalization.base import BaseNormalizer

class QRadarNormalizer(BaseNormalizer):
    source_type = "qradar"

    def normalize(self):
        raw = self.raw_data
        return {
            "source_type": self.source_type,
            "alert_severity": self.map_severity(raw.get("severity")),
            "status": self.map_status(raw.get("status")),
            "reason": raw.get("description", "N/A"),
            "rule": ", ".join(r.get("name", "") for r in raw.get("rules", [])) or "Unknown Rule",
            "source_ip": raw.get("offense_source"),
            "destination_ip": None,
            "user_name": None,
            "host_name": None,
            "time_stamp": raw.get("start_time"),
            "raw": raw
        }
