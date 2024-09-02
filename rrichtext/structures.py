from dataclasses import dataclass

from .base import JSONType, _ElementNode, _parse_element, _parse_element_list
from .media import AnimatedImage, Image
from .reddit import _RedditLink
from .text import Link, RawText, SpoilerText, Text, _TextNode

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


@dataclass
class CodeBlock(_ElementNode):
    content: list["RawText"]
    language: str | None = None

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"e": self._e, "c": [c.to_jobj() for c in self.content]}
        if self.language:
            r["l"] = self.language
        return r

    @classmethod
    def parse(cls, obj: JSONType) -> "CodeBlock":
        cls._validate(obj)
        return cls(
            _parse_element_list(cls._get_jobj_value(obj, "c", list), RawText),
            cls._get_jobj_value(obj, "l", str, True),
        )


CodeBlock._e = "code"


_TableCellText = Text | Link | _RedditLink | SpoilerText | Image | AnimatedImage


@dataclass
class TableHeaderCell:
    content: list[_TableCellText]
    alignment: str | None = None

    @classmethod
    def parse(cls, obj: JSONType) -> "TableHeaderCell":
        return cls(
            _parse_element_list(_ElementNode._get_jobj_value(obj, "c", list), _TableCellText),
            _ElementNode._get_jobj_value(obj, "a", str, True),
        )

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"c": [c.to_jobj() for c in self.content]}
        if self.alignment:
            r["a"] = self.alignment
        return r


@dataclass
class TableCell:
    content: list[_TableCellText]

    @classmethod
    def parse(cls, obj: JSONType) -> "TableCell":
        return cls(
            _parse_element_list(_ElementNode._get_jobj_value(obj, "c", list), _TableCellText),
        )

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"c": [c.to_jobj() for c in self.content]}
        return r


@dataclass
class TableRow:
    content: list[TableCell]

    @classmethod
    def parse(cls, obj: list[JSONType]) -> "TableRow":
        return cls([TableCell.parse(e) for e in obj])

    def to_jobj(self) -> JSONType:
        return [c.to_jobj() for c in self.content]


@dataclass
class Table(_ElementNode):
    headerContent: list[TableHeaderCell]
    rowContent: list[TableRow]

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {
            "e": self._e,
            "h": [c.to_jobj() for c in self.headerContent],
            "c": [c.to_jobj() for c in self.rowContent],
        }
        return r

    @classmethod
    def parse(cls, obj: JSONType) -> "Table":
        cls._validate(obj)
        return cls(
            [TableHeaderCell.parse(e) for e in cls._get_jobj_value(obj, "h", list)],
            [TableRow.parse(e) for e in cls._get_jobj_value(obj, "c", list)],
        )


Table._e = "table"


_ListChild = Heading | List | Paragraph | BlockQuote | CodeBlock | Table  # | HorizontalRule

_BlockQuoteNode = BlockQuote | Heading | List | Paragraph | CodeBlock | Table
