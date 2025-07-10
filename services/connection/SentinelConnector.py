import requests
from services.connection.base import BaseConnector

class SentinelConnector(BaseConnector):
    source_type = "sentinel"

    def __init__(self, tenant_id, client_id, client_secret, workspace_id):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.workspace_id = workspace_id

    def _get_token(self):
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"
        data = {
            "grant_type": "client_credentials",
            "resource": "https://management.azure.com/",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def connect(self):
        token = self._get_token()
        url = f"https://management.azure.com/subscriptions/{self.workspace_id}/providers/Microsoft.SecurityInsights/incidents?api-version=2020-01-01"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("value", [])