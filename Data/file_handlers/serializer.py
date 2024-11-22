from abc import ABC, abstractmethod
from Transports import Transport

# Тип данных TransportsData
TransportsData = dict[str, int | list[Transport]]

class Serializer(ABC):

    @abstractmethod
    def to_format(self, transports_data: TransportsData) -> str:
        """
        Метод для сериализации данных о транспортах в строку.
        :param transports_data: Данные о транспортах.
        :return: Строка в заданном формате.
        """
        pass

    @abstractmethod
    def from_format(self, file_data: str) -> TransportsData:
        """
        Метод для десериализации строки в данные о транспортах.
        :param file_data: Строка с данными о транспортах в заданном формате.
        :return: Объект TransportsData.
        """
        pass

    @abstractmethod
    def get_type(self) -> str:
        """
        Метод для получения типа формата.
        :return: Название формата данных.
        """
        pass
