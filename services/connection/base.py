from abc import ABC, abstractmethod

class BaseConnector(ABC):
    def __init__(self, credentials,timestamp):
        self.credentials = credentials
        self.timestamp = timestamp
    @abstractmethod
    def connect(self):
        pass