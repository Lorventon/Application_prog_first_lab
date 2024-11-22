from Data.file_handlers.json_handler import JSONSerializer
from Transports import Car
from const import FilePathEnum


def main() -> None:
    car = Car("Bmw", 1, "m5", "red")
    transports = [car]
    serializer = JSONSerializer()
    print(serializer.to_format(transports))


if __name__ == "__main__":
    main()
