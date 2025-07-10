import requests
from services.connection.base import BaseConnector

class QRadarConnector(BaseConnector):
    source_type = "qradar"

    def __init__(self, host, token, verify_ssl=True):
        self.host = host
        self.token = token
        self.verify_ssl = verify_ssl

    def connect(self):
        url = f"{self.host}/api/siem/offenses"
        headers = {
            "SEC": self.token,
            "Accept": "application/json"
        }
        params = {"filter": "status!=CLOSED"}
        response = requests.get(url, headers=headers, params=params, verify=self.verify_ssl)
        response.raise_for_status()
        return response.json()