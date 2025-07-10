from .base import BaseNormalizer
from datetime import datetime

class ElasticNormalizer(BaseNormalizer):
    source_type = "elastic"

    def normalize(self):
        raw = self.raw_data

        return {
            "source_type": self.source_type,
            "alert_id":raw.get("id", ""),
            "rule": raw.get("kibana.alert.rule.name", ""),
            "alert_severity": raw.get("kibana.alert.severity", "").capitalize(),
            "reason": raw.get("kibana.alert.reason", "N/A"),
            "source_ip": raw.get("source", {}).get("ip"),
            "timeStamp": raw.get("@timestamp"),
            "destination_ip": raw.get("destination", {}).get("ip"),
            "destination_port": raw.get("destination", {}).get("port"),
            "source_port": raw.get("source", {}).get("port"),
            "event_action": raw.get("event", {}).get("action"),
            "firewall_action": raw.get("fortinet", {}).get("firewall", {}).get("action"),
            "firewall_attack": raw.get("fortinet", {}).get("firewall", {}).get("attack"),
            "host_name": raw.get("host", {}).get("name"),
            "user_name": raw.get("user", {}).get("name"),
            "file_name": raw.get("file", {}).get("name"),
            "process_name": raw.get("process", {}).get("name"),
            "process_command_line": raw.get("process", {}).get("command_line"),
            "url_query": raw.get("url", {}).get("query"),
            "s1_description": raw.get("sentinel_one", {}).get("threat", {}).get("analysis", {}).get("description"),
            "s1_mitigation_mode": raw.get("sentinel_one", {}).get("threat", {}).get("detection", {}).get("agent", {}).get("mitigation_mode"),
            "s1_threat_name": raw.get("sentinel_one", {}).get("threat", {}).get("name"),
            "threat_indicator_file_path": raw.get("threat", {}).get("indicator", {}).get("file", {}).get("path"),
            "related_hash": raw.get("related", {}).get("hash"),
            "endpoint_sha256": raw.get("Endpoint", {}).get("policy", {}).get("applied", {}).get("artifacts", {}).get("global", {}).get("identifiers", {}),
            "file_hash_md5": raw.get("file", {}).get("hash", {}).get("md5"),
            "file_path": raw.get("file", {}).get("path"),
            "file_owner": raw.get("file", {}).get("owner"),
            "network_bytes": raw.get("network", {}).get("bytes"),
            "source_bytes": raw.get("source", {}).get("bytes"),
            "destination_bytes": raw.get("destination", {}).get("bytes"),
            "event_duration": raw.get("event", {}).get("duration"),
            "source_org": raw.get("source", {}).get("as", {}).get("organization", {}).get("name"),
            
        }


    