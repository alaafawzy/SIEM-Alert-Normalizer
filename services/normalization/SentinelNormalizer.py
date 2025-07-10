from services.normalization.base import BaseNormalizer


class SentinelNormalizer(BaseNormalizer):

    source_type = "sentinel"

    def normalize(self):
        raw = self.raw_data
        props = raw.get("properties", {})
        status = self.STATUS_MAP.get(props.get("status", "New"), "Reported")
        severity = self.SEVERITY_MAP.get(props.get("severity", "Low"), "Low")
        return {
            "source_type": "Azure Sentinel",
            "alert_severity": severity,  # Assuming it matches your choices
            "status": status,
            "reason": props.get("classificationReason", "N/A"),
            "user_name": props.get("owner", {}).get("userPrincipalName"),
            "timeStamp": props.get("createdTimeUtc", None),
            "host_name": props.get("incidentUrl", None),
            "title": props.get("title", ""),
            "classification": props.get("classification", ""),
            "classificationComment": props.get("classificationComment", "Not a malicious activity"),
            "description": props.get("description", ""),
            "providerIncidentId": props.get("providerIncidentId", ""),
            "providerName": props.get("providerName", "")
        }

    # field_mapping_sentinel = {
    #     "timestamp": "TimeGenerated",
    #     "alert_reason": "ExtendedProperties.AlertReason",  # or custom/parsed from AlertDetails
    #     "alert_rule_name": "AlertName",
    #     "alert_severity": "Severity",
    #     "destination_ip": "DestinationIP",
    #     "source_ip": "SourceIP",
    #     "destination_port": "DestinationPort",
    #     "source_port": "SourcePort",
    #     "event_action": "Action",
    #     "firewall_action": "DeviceAction",
    #     "firewall_attack": "ThreatName",  # or parsed from Custom Fields
    #     "host_name": "Computer",
    #     "user_name": "Account",
    #     "file_name": "FileName",
    #     "process_name": "ProcessName",
    #     "process_command_line": "CommandLine",
    #     "url_query": "Url",  # can also be in `RequestUrl` or split parts
    #     "s1_description": "ThreatDescription",  # CustomEntity or ExtendedProperties
    #     "s1_mitigation_mode": "MitigationMode",  # often custom field
    #     "s1_threat_name": "ThreatName",
    #     "threat_indicator_file_path": "FilePath",
    #     "related_hash": "Hashes",  # often includes MD5/SHA256 etc.
    #     "endpoint_sha256": "SHA256",
    #     "file_hash_md5": "MD5",
    #     "file_path": "FilePath",
    #     "file_owner": "FileOwner",  # could be in `AdditionalFields`
    #     "network_bytes": "NetworkBytes",  # or calculated from `SentBytes` + `ReceivedBytes`
    #     "source_bytes": "SentBytes",
    #     "destination_bytes": "ReceivedBytes",
    #     "event_duration": "DurationMs",
    #     "source_org": "SourceIPLocation.Organization",  # parsed from IP enrichment
    # }

    STATUS_MAP = {
        "New": "Reported",
        "Active": "Investigation",
        "Closed": "Remediated",
    }

    SEVERITY_MAP = {
        "Low": "Low",
        "Medium": "Medium",
        "High": "High",
        "Informational": "Low",
    }