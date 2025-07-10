from datetime import datetime

from services.connection.base import BaseConnector


class SentinelConnector(BaseConnector):
    source_type = "sentinel"

    def connect(self):
        print("implement connection methodology")
