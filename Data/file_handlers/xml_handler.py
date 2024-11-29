from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom.minidom import parseString

from serializer import Serializer
from Transports import Transport


class XmlSerializer(Serializer):

    def to_format(self, transports: list) -> str:
        serializable_data = [transport.to_dict() for transport in transports]
        root = Element("transports_data")
        total_count = SubElement(root, "total_count")
        total_count.text = str(transports_data.get("total_count", 0))

        transports_element = SubElement(root, "transports")
        for transport in transports_data.get("transports", []):
            transport_element = SubElement(transports_element, "transport")
            for key, value in transport.to_dict().items():
                child = SubElement(transport_element, key)
                child.text = str(value)

        raw_xml = tostring(root, encoding='unicode')

        dom = parseString(raw_xml)
        pretty_xml = dom.toprettyxml(indent="    ")
        return pretty_xml

    def from_format(self, file_data: str) -> list:
        root = fromstring(file_data)
        transports = []
        total_count = int(root.find("total_count").text)

        for transport_element in root.find("transports"):
            transport_data = {child.tag: child.text for child in transport_element}
            transport_data["transport_id"] = int(transport_data["transport_id"])
            transport_data["capacity"] = int(transport_data["capacity"])
            transport = Transport.from_dict(transport_data)
            transports.append(transport)

        return {"total_count": total_count, "transports": transports}

    def get_type(self) -> str:
        return "xml"
