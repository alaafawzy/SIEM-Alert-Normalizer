from abc import ABC, abstractmethod

class BaseNormalizer(ABC):
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @abstractmethod
    def normalize(self):
        pass