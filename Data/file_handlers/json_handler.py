import json

from Data.file_handlers.serializer import Serializer
from Transports import Transport, TRANSPORT_MAP


class JSONSerializer(Serializer):

    def to_format(self, transports: list) -> str:
        serializable_data = [transport.to_dict() for transport in transports]
        return json.dumps(serializable_data, indent=4)

    def from_format(self, file_data: str) -> list:
        raw_data = json.loads(file_data)
        transports = []
        for transport_data in raw_data:
            if transport_data["type_of_transport"] is not TRANSPORT_MAP:
                raise TypeError()
            transport = TRANSPORT_MAP[transport_data["type_of_transport"]](transport_data["name"],
                                                                           transport_data["speed"])
            transports.append(transport)
        return transports

    def get_type(self) -> str:
        return "json"


