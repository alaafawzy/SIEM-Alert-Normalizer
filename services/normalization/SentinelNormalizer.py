from services.normalization.base import BaseNormalizer

class SentinelNormalizer(BaseNormalizer):
    source_type = "sentinel"

    def normalize(self):
        props = self.raw_data.get("properties", {})
        owner = props.get("owner", {})
        return {
            "source_type": self.source_type,
            "alert_severity": self.map_severity(props.get("severity")),
            "status": self.map_status(props.get("status")),
            "reason": props.get("classificationReason", "N/A"),
            "rule": props.get("title", "Unknown Rule"),
            "source_ip": None,
            "destination_ip": None,
            "user_name": owner.get("userPrincipalName"),
            "host_name": props.get("incidentUrl"),
            "time_stamp": props.get("createdTimeUtc"),
            "raw": self.raw_data
        }
