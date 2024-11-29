from const import TransportEnum

TRANSPORT_MAP = {
    'Car': lambda name, speed, color, model: Car(name, speed, model, color),
    'Bike': lambda name, speed, color: Bike(name, speed, color),
    'Bus': lambda name, speed, color, passenger_capacity: Bus(name, speed, passenger_capacity, color),
    'Truck': lambda name, speed, color, load_capacity: Truck(name, speed, load_capacity, color),
    'Motorcycle': lambda name, speed, color, model: Motorcycle(name, speed, model, color),
}

transports = list()


class Transport:

    def __init__(self, type_of_transport: str, name: str, speed: int, color: str) -> None:
        if type_of_transport not in TRANSPORT_MAP:
            raise ValueError(f"Invalid type of transport: {type_of_transport}")

        self.__transport_id: int = 0
        self.__name: str = name
        self.__type_of_transport: str = type_of_transport
        self.__speed: int = speed
        self.__color: str = color

    @property
    def transport_id(self) -> int:
        return self.__transport_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def type_of_transport(self) -> str:
        return self.__type_of_transport

    @property
    def speed(self) -> int:
        return self.__speed

    @property
    def color(self) -> str:
        return self.__color

    @transport_id.setter
    def transport_id(self, id: int) -> None:
        self.__transport_id = id

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @type_of_transport.setter
    def type_of_transport(self, type_of_transport: TransportEnum) -> None:
        self.__type_of_transport = type_of_transport

    @speed.setter
    def speed(self, speed: int) -> None:
        self.__speed = speed

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color

    def to_dict(self) -> dict:
        return {
            "type_of_transport": self.__type_of_transport,
            "transport_id": self.__transport_id,
            "name": self.__name,
            "speed": self.__speed,
            "color": self.__color
        }

    @staticmethod
    def from_dict(data: dict) -> "Transport":
        transport = Transport(data["type_of_transport"], data["name"], data["speed"], data["color"])
        transport.transport_id = data.get("transport_id", 0)
        return transport

    def __str__(self) -> str:
        return f"{self.type_of_transport}  {self.name}, speed: {self.speed}"


class Car(Transport):
    def __init__(self, name: str, speed: int, color: str, model: str) -> None:
        super().__init__(Car.__name__, name, speed, color)
        self.model: str = model

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["model"] = self.model
        return data

    @staticmethod
    def from_dict(data: dict) -> "Car":
        car = Car(data["name"], data["speed"], data["model"], data["color"])
        car.transport_id = data.get("transport_id", 0)
        return car


class Bike(Transport):
    def __init__(self, name: str, speed: int, color: str) -> None:
        super().__init__(TransportEnum.BIKE.value, name, speed, color)

    def to_dict(self) -> dict:
        data = super().to_dict()
        return data

    @staticmethod
    def from_dict(data: dict) -> "Bike":
        bike = Bike(data["name"], data["speed"], data["color"])
        bike.transport_id = data.get("transport_id", 0)
        return bike


class Bus(Transport):
    def __init__(self, name: str, speed: int, color: str, passenger_capacity: int) -> None:
        super().__init__(TransportEnum.BUS.value, name, speed, color)
        self.passenger_capacity: int = passenger_capacity

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["passenger_capacity"] = self.passenger_capacity
        return data

    @staticmethod
    def from_dict(data: dict) -> "Bus":
        bus = Bus(data["name"], data["speed"], data["passenger_capacity"], data["color"])
        bus.transport_id = data.get("transport_id", 0)
        return bus


class Truck(Transport):
    def __init__(self, name: str, speed: int, color: str, load_capacity: int) -> None:
        super().__init__(TransportEnum.TRUCK.value, name, speed, color)
        self.load_capacity: int = load_capacity

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["load_capacity"] = self.load_capacity
        return data

    @staticmethod
    def from_dict(data: dict) -> "Truck":
        truck = Truck(data["name"], data["speed"], data["load_capacity"], data["color"])
        truck.transport_id = data.get("transport_id", 0)
        return truck


class Motorcycle(Transport):
    def __init__(self, name: str, speed: int, color: str, model: str):
        super().__init__(TransportEnum.MOTORCYCLE.value, name, speed, color)
        self.model: str = model

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["model"] = self.model
        return data

    @staticmethod
    def from_dict(data: dict) -> "Motorcycle":
        motorcycle = Motorcycle(data["name"], data["speed"], data["model"], data["color"])
        motorcycle.transport_id = data.get("transport_id", 0)
        return motorcycle

