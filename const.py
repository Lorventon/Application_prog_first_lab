from enum import Enum

JSON_DB_PATH = '../DataBase/JSON/transport_db.json'
XML_DB_PATH = '../DataBase/XML/transport_db.xml'


class FilePathEnum(Enum):
    JSON = JSON_DB_PATH
    XML = XML_DB_PATH

    @staticmethod
    def get_path(data_format: str) -> str:
        try:
            return FilePathEnum[data_format.upper()].value
        except KeyError:
            raise ValueError(
                f"Invalid file format: {data_format}. Available formats: {', '.join([f.name.lower() for f in FilePathEnum])}")


class TransportEnum(Enum):
    CAR = "Car"
    BIKE = "Bike"
    BUS = "Bus"
    TRUCK = "Truck"
    MOTORCYCLE = "Motorcycle"

    @staticmethod
    def is_valid_type(value: str) -> bool:
        return value.lower() in [transport_type.value.lower() for transport_type in TransportEnum]
