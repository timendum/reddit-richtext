from dataclasses import dataclass

from .base import JSONType, _ElementNode, _parse_element, _parse_element_list
from .media import AnimatedImage, Image
from .reddit import _RedditLink
from .text import Link, RawText, _TextNode

_ParagraphContentNode = _TextNode | Image | AnimatedImage


@dataclass
class Paragraph(_ElementNode):
    content: list[_ParagraphContentNode]

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "c": [e.to_jobj() for e in self.content]}

    @classmethod
    def parse(cls, obj: JSONType) -> "Paragraph":
        cls._validate(obj)
        return cls(_parse_element_list(cls._get_jobj_value(obj, "c", list), _ParagraphContentNode))


Paragraph._e = "par"


_HeadingText = RawText | Link | _RedditLink


@dataclass
class Heading(_ElementNode):
    level: int
    content: list[_HeadingText]

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "l": self.level, "c": [e.to_jobj() for e in self.content]}

    @classmethod
    def parse(cls, obj: JSONType) -> "Heading":
        cls._validate(obj)
        return cls(
            cls._get_jobj_value(obj, "l", int),
            _parse_element_list(cls._get_jobj_value(obj, "c", list), _HeadingText),
        )


Heading._e = "h"


@dataclass
class ListElement(_ElementNode):
    content: list["_ListChild"]

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "c": [e.to_jobj() for e in self.content]}

    @classmethod
    def parse(cls, obj: JSONType) -> "ListElement":
        cls._validate(obj)
        return cls(
            _parse_element_list(cls._get_jobj_value(obj, "c", list), _ListChild),
        )


ListElement._e = "li"


@dataclass
class List(_ElementNode):
    ordered: bool
    content: list[ListElement]

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "o": self.ordered, "c": [e.to_jobj() for e in self.content]}

    @classmethod
    def parse(cls, obj: JSONType) -> "List":
        cls._validate(obj)
        return cls(
            cls._get_jobj_value(obj, "o", bool),
            _parse_element_list(cls._get_jobj_value(obj, "c", list), ListElement),
        )


List._e = "list"


@dataclass
class BlockQuote(_ElementNode):
    content: list["_BlockQuoteNode"]
    author: _TextNode | None = None

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"e": self._e, "c": [c.to_jobj() for c in self.content]}
        if self.author:
            r["a"] = self.author.to_jobj()
        return r

    @classmethod
    def parse(cls, obj: JSONType) -> "BlockQuote":
        cls._validate(obj)
        a = cls._get_jobj_value(obj, "a", dict, True)
        return cls(
            _parse_element_list(cls._get_jobj_value(obj, "c", list), _BlockQuoteNode),
            _parse_element(a, _TextNode) if a else None,
        )


BlockQuote._e = "blockquote"

_ListChild = Heading | List | Paragraph | BlockQuote  # CodeBlock |  HorizontalRule | Table

_BlockQuoteNode = BlockQuote | Heading | List | Paragraph  # | CodeBlock | Table;
