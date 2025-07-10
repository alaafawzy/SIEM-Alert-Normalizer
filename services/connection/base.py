import abc

class BaseConnector(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        """Connect to the SIEM and return raw alerts"""
        pass