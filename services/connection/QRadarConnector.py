from datetime import datetime

from services.connection.base import BaseConnector


class QRadarConnector(BaseConnector):
    source_type = "qradar"

    def connect(self):
        print("implement connection methodology")
