import json
from Transports import Transport
from serializer import Serializer
from serializer import TransportsData


class JSONSerializer(Serializer):

    def to_format(self, transports_data: TransportsData) -> str:
        serializable_data = {
            "total_count": transports_data["total_count"],
            "transports": [
                transport.to_dict() for transport in transports_data["transports"]
            ]
        }
        return json.dumps(serializable_data, ensure_ascii=False, indent=4)

    def from_format(self, file_data: str) -> TransportsData:
        raw_data = json.loads(file_data)
        return {
            "total_count": raw_data["total_count"],
            "transports": [
                Transport.from_dict(item) for item in raw_data["transports"]
            ]
        }

    def get_type(self) -> str:
        return "json"
