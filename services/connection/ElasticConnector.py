from elasticsearch import Elasticsearch
from services.connection.base import BaseConnector

class ElasticConnector(BaseConnector):
    source_type = "elastic"

    def __init__(self, hosts, username, password):
        self.client = Elasticsearch(
            hosts,
            basic_auth=(username, password)
        )

    def connect(self, index, query):
        result = self.client.search(index=index, body=query)
        hits = result.get("hits", {}).get("hits", [])
        return [hit["_source"] for hit in hits]