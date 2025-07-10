import pytest
from services.normalization.normalization_factory import NormalizationFactory

# Example raw samples for unit testing:
qradar_sample = {"description": "Test QRadar", "severity": 2, "status": "OPEN", "rules": [{"name": "Test Rule"}], "offense_source": "192.168.1.5", "start_time": "2025-07-10T12:00:00Z"}
sentinel_sample = {"properties": {"title": "Test Sentinel", "severity": "Medium", "status": "New", "classificationReason": "Suspicious", "owner": {"userPrincipalName": "user@example.com"}, "incidentUrl": "http://sentinel/incident", "createdTimeUtc": "2025-07-10T12:00:00Z"}}
elastic_sample = {"message": "Test Elastic", "@timestamp": "2025-07-10T12:00:00Z", "event": {"severity": "high", "status": "open", "rule": {"name": "Test Rule"}}, "source": {"ip": "10.0.0.1"}, "destination": {"ip": "10.0.0.2"}, "user": {"name": "elastic_user"}, "host": {"name": "elastic_host"}}

@pytest.mark.parametrize("source_type, sample", [
    ("qradar", qradar_sample),
    ("sentinel", sentinel_sample),
    ("elastic", elastic_sample)
])
def test_normalizer_fields(source_type, sample):
    normalizer = NormalizationFactory.get_normalizer(source_type, sample)
    normalized = normalizer.normalize()
    expected_keys = ["source_type", "alert_severity", "status", "reason", "rule", "source_ip", "destination_ip", "user_name", "host_name", "time_stamp", "raw"]
    for key in expected_keys:
        assert key in normalized, f"{key} missing in {source_type} normalized output"
