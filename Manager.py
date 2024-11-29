from Data import Storage
from Transports import TRANSPORT_MAP


class TransportService():
    def __init__(self, storage: Storage) -> None:
        self.__storage = storage
        self.__transports = []

    def create_transport(self, type_of_transport: str, name: str, speed: int, color: str, ) -> None:
        if type_of_transport not in TRANSPORT_MAP:
            raise TypeError
        transport = TRANSPORT_MAP[type_of_transport](name, speed, color)
        self.__transports.append(transport)
        self.__storage.save_to_file(self.__transports)
        print("Транспорт успешно добавлен.")

