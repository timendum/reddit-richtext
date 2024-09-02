from dataclasses import dataclass
from dataclasses import field as dcfield

from .base import FormatRange, JSONType, LineBreak, _ElementNode, _parse_element_list
from .reddit import _RedditLink


@dataclass
class Text(_ElementNode):
    text: str
    formattings: list[FormatRange] = dcfield(default_factory=list)

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"e": self._e, "t": self.text}
        FormatRange.add_jobj_formattings(self, r)
        return r

    @classmethod
    def parse(cls, obj: JSONType) -> "Text":
        cls._validate(obj)
        return cls(
            cls._get_jobj_value(obj, "t", str),
            FormatRange.parse_formatRange(obj),
        )


Text._e = "text"


@dataclass
class Link(_ElementNode):
    text: str
    url: str
    formattings: list[FormatRange] = dcfield(default_factory=list)
    tooltip: str = ""

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"e": self._e, "t": self.text, "u": self.url}
        if self.formattings:
            r["f"] = [x.to_jobj() for x in self.formattings]
        if self.tooltip:
            r["a"] = self.tooltip
        return r

    @classmethod
    def parse(cls, obj: JSONType) -> "Link":
        cls._validate(obj)
        return cls(
            cls._get_jobj_value(obj, "t", str),
            cls._get_jobj_value(obj, "u", str),
            FormatRange.parse_formatRange(obj),
            cls._get_jobj_value(obj, "a", str, True) or "",
        )


Link._e = "link"


_PlainText = Text | Link | _RedditLink | LineBreak


@dataclass
class SpoilerText(_ElementNode):
    content: list[_PlainText] = dcfield(default_factory=list)

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "c": [e.to_jobj() for e in self.content]}

    @classmethod
    def parse(cls, obj: JSONType) -> "SpoilerText":
        cls._validate(obj)
        return cls(_parse_element_list(cls._get_jobj_value(obj, "c", list), _PlainText))


SpoilerText._e = "spoilertext"

_TextNode = _PlainText | SpoilerText


@dataclass
class RawText(_ElementNode):
    text: str

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"e": self._e, "t": self.text}
        return r

    @classmethod
    def parse(cls, obj: JSONType) -> "RawText":
        cls._validate(obj)
        return cls(
            cls._get_jobj_value(obj, "t", str),
        )


RawText._e = "raw"
