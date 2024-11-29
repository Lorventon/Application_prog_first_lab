import os
from file_handlers.serializer import Serializer
from const import FilePathEnum
from typing import Dict, List
from Transports import Transport


class TransportStorage:
    def __init__(self, serializer: Serializer) -> None:
        self.serializer: Serializer = serializer
        self.db_path: str = FilePathEnum.get_path(serializer.get_type())

    def save_to_file(self, transports: list) -> None:
        try:
            if not os.path.exists(self.db_path):
                self._create_file(self.db_path)
            with open(self.db_path, 'w', encoding='utf-8') as file:
                #Необходим список транпспортов.
                file.write(self.serializer.to_format(transports))
                print(f"Данные сохранены в файл: {self.db_path}")
        except Exception as error:
            print(f"Ошибка при сохранении данных: {error}")

    def load_from_file(self) -> list:

        try:
            if not os.path.exists(self.db_path):
                self._create_file()
            with open(self.db_path, 'r', encoding='utf-8') as file:
                return self.serializer.from_format(file.read())
        except Exception as error:
            print(f"Ошибка при загрузке данных: {error}")
            return {"total_count": 0, "transports": []}

    def _create_file(self) -> None:
        print(f"Создание нового файла: {self.db_path}")
        initial_data: list = {"transports": []}
        with open(self.db_path, 'w', encoding='utf-8') as file:
            file.write(self.serializer.to_format(initial_data))
