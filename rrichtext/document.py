import json
from dataclasses import dataclass

from .base import HorizontalRule, JSONType, RTDecodeError, _parse_element_list
from .media import _Media
from .structures import BlockQuote, CodeBlock, Embed, Heading, List, Paragraph, Table

_DocumentNode = (
    Paragraph | Heading | HorizontalRule | BlockQuote | CodeBlock | Embed | List | Table | _Media
)


@dataclass
class RichTextContent:
    document: list[_DocumentNode]

    def to_jobj(self) -> JSONType:
        return {"document": [d.to_jobj() for d in self.document]}

    def to_json(self) -> str:
        return json.dumps(self.to_jobj())

    @classmethod
    def parse_jobj(cls, obj: JSONType) -> "RichTextContent":
        if (
            not isinstance(obj, dict)
            or "document" not in obj
            or not isinstance(obj["document"], list)
        ):
            raise RTDecodeError("obj not a RichTextContent", obj)
        content = _parse_element_list(obj["document"], _DocumentNode)
        return cls(content)

    @classmethod
    def parse(cls, s):
        obj = json.loads(s)
        return cls.parse_jobj(obj)
