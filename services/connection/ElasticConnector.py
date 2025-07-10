from datetime import datetime
from elasticsearch import Elasticsearch
from services.connection.base import BaseConnector
from utils.response import error_response


class ElasticConnector(BaseConnector):
    source_type = "elastic"

    def connect(self):
        try:
            es = Elasticsearch(
                hosts=[self.credentials.host],
                api_key=(self.credentials.api_key_id, self.credentials.api_key),
                verify_certs=True
            )
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Elasticsearch: {e}")

        try:
            query = {
                "query": {
                    "range": {
                        "@timestamp": {
                            "gt": self.timestamp
                        }
                    }
                },
            }
            response = es.search(
                index=".internal.alerts-security.alerts-default-*",
                body=query,
                size=1000
            )

            alerts = [
                {
                    **hit['_source'],
                    'id': hit['_id']
                }
                for hit in response['hits']['hits']
            ]

            return alerts
        except Exception as e:
            raise RuntimeError(f"Error querying Elasticsearch: {e}")
