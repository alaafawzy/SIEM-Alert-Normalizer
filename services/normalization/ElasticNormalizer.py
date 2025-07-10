from services.normalization.base import BaseNormalizer

class ElasticNormalizer(BaseNormalizer):
    source_type = "elastic"

    def normalize(self):
        raw = self.raw_data
        event = raw.get("event", {})
        source = raw.get("source", {})
        destination = raw.get("destination", {})
        user = raw.get("user", {})
        host = raw.get("host", {})
        return {
            "source_type": self.source_type,
            "alert_severity": self.map_severity(event.get("severity")),
            "status": self.map_status(event.get("status")),
            "reason": raw.get("message", "N/A"),
            "rule": event.get("rule", {}).get("name", "Unknown Rule"),
            "source_ip": source.get("ip"),
            "destination_ip": destination.get("ip"),
            "user_name": user.get("name"),
            "host_name": host.get("name"),
            "time_stamp": raw.get("@timestamp"),
            "raw": raw
        }
