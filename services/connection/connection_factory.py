from services.connection.QRadarConnector import QRadarConnector
from services.connection.SentinelConnector import SentinelConnector
from services.connection.ElasticConnector import ElasticConnector

class ConnectionFactory:
    @staticmethod
    def get_connector(source_type, **kwargs):
        connectors = {
            "qradar": QRadarConnector,
            "sentinel": SentinelConnector,
            "elastic": ElasticConnector
        }
        connector_cls = connectors.get(source_type.lower())
        if connector_cls:
            return connector_cls(**kwargs)
        raise ValueError(f"Unsupported source type: {source_type}")
