from abc import ABC, abstractmethod
from Transports import Transport


class Serializer(ABC):

    @abstractmethod
    def to_format(self, transports: list) -> str:
        pass

    @abstractmethod
    def from_format(self, file_data: str) -> list:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass
