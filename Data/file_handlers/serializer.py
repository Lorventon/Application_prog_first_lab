from abc import ABC, abstractmethod
from Transports import Transport

TransportsData = dict[str, int | list[Transport]]


class Serializer(ABC):

    @abstractmethod
    def to_format(self, transports_data: TransportsData) -> str:
        pass

    @abstractmethod
    def from_format(self, file_data: str) -> TransportsData:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass
