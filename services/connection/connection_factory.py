from services.connection.ElasticConnector import ElasticConnector
from services.connection.QRadarConnector import QRadarConnector
from services.connection.SentinelConnector import SentinelConnector

NORMALIZER_MAP = {
    "qradar": QRadarConnector,
    "sentinel": SentinelConnector,
    "elastic": ElasticConnector
    # Add more mappings here
}

def get_Connector(source_type, credentials,timestamp):
    connector_class = NORMALIZER_MAP.get(source_type)
    if not connector_class:
        raise ValueError(f"No connector found for source type: {source_type}")
    return connector_class(credentials,timestamp)