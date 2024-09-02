import json
from dataclasses import dataclass
from types import UnionType
from typing import Any, ClassVar, cast

JSONType = dict[str, "JSONType"] | list["JSONType"] | str | int | float | bool | None


class RTDecodeError(ValueError):
    """Subclass of ValueError with the following additional properties:

    msg: The unformatted error message
    doc: The JSON document being parsed

    """

    def __init__(self, msg, doc):
        ValueError.__init__(self, msg)
        self.doc = doc


@dataclass
class _ElementNode:
    _e: ClassVar[str]

    def to_jobj(self) -> JSONType:  # pragma: no cover
        pass

    def to_json(self) -> str:  # pragma: no cover
        return json.dumps(self.to_jobj())

    @classmethod
    def _validate(cls, obj: JSONType) -> None:
        if not isinstance(obj, dict) or "e" not in obj or obj["e"] != cls._e:
            raise RTDecodeError("Wrong e tag value", obj)

    @staticmethod
    def _get_jobj_value(obj: JSONType, key: str, classinfo, optional=False) -> Any:
        if not isinstance(obj, dict) or key not in obj:
            if not optional:
                raise RTDecodeError("obj not a valid", obj)
            return None
        if not isinstance(obj[key], classinfo):
            raise RTDecodeError(f"obj not a valid: got {type(obj[key])} expecting {classinfo}", obj)
        return obj.get(key, None)

    @classmethod
    def parse(cls, obj: JSONType) -> "_ElementNode":  # pragma: no cover
        return _ElementNode()


@dataclass
class FormatRange:
    f: int
    t: int
    bold: bool = False
    italic: bool = False
    underline: bool = False
    strikethrough: bool = False
    subscript: bool = False
    superscript: bool = False
    monospace: bool = False

    @property
    def formattingFlag(self) -> int:
        return (
            1 * self.bold
            + 2 * self.italic
            + 4 * self.underline
            + 8 * self.strikethrough
            + 16 * self.subscript
            + 32 * self.superscript
            + 64 * self.monospace
        )

    def to_jobj(self) -> JSONType:
        return [self.formattingFlag, self.f, self.t]

    @classmethod
    def parse(cls, obj: JSONType):
        if not isinstance(obj, list) or len(obj) != 3:
            raise RTDecodeError("obj not a FormatRange", obj)
        formattingFlag, f, t = obj
        if not isinstance(formattingFlag, int) or not isinstance(f, int) or not isinstance(t, int):
            raise RTDecodeError("obj not a FormatRange", obj)
        return cls(
            f,
            t,
            bool(formattingFlag & 1),
            bool(formattingFlag & 2),
            bool(formattingFlag & 4),
            bool(formattingFlag & 8),
            bool(formattingFlag & 16),
            bool(formattingFlag & 32),
            bool(formattingFlag & 64),
        )

    @classmethod
    def fill_text(cls, e: _ElementNode, key: str = "text") -> "FormatRange":
        text = getattr(e, key)
        f = cls(
            0,
            len(text),
        )
        if hasattr(e, "formattings"):
            e.formattings = [f]  # type: ignore
        else:
            raise ValueError("Element does not support formatting")
        return f

    @staticmethod
    def add_jobj_formattings(e: _ElementNode, jobj: dict[str, JSONType]) -> None:
        formattings = getattr(e, "formattings", None)
        if formattings:
            jobj["f"] = [x.to_jobj() for x in formattings]

    @classmethod
    def parse_formatRange(cls, obj: JSONType) -> list["FormatRange"]:
        if not isinstance(obj, dict) or not isinstance(obj.get("f", None), list):
            return []
        return [cls.parse(e) for e in cast(str, obj["f"])]


def _parse_element_list(objs_list: JSONType, parent_class: UnionType | type) -> list[Any]:
    elements = []
    if not isinstance(objs_list, list):
        raise RTDecodeError("Object not a list", objs_list)
    for obj in objs_list:
        elements.append(_parse_element(obj, parent_class))
    return elements


def _parse_element(obj: JSONType, parent_class: UnionType | type) -> Any:
    tags = {cls._e: cls for cls in _ElementNode.__subclasses__()}
    if not isinstance(obj, dict) or not isinstance(obj.get("e", None), str):
        raise RTDecodeError("Object not a valid node", obj)
    try:
        subclass = tags[cast(str, obj["e"])]
    except KeyError as err:
        raise RTDecodeError("Element not handled: " + str(obj["e"]), obj) from err
    if not issubclass(subclass, parent_class):
        raise RTDecodeError(
            f"Element not expected: got {subclass} but expected {parent_class}", obj
        )
    return subclass.parse(obj)


@dataclass
class LineBreak(_ElementNode):
    def to_jobj(self) -> JSONType:
        return {"e": self._e}

    @classmethod
    def parse(cls, obj: JSONType) -> "LineBreak":
        cls._validate(obj)
        return cls()


LineBreak._e = "br"


@dataclass
class HorizontalRule(_ElementNode):
    def to_jobj(self) -> JSONType:
        return {"e": self._e}

    @classmethod
    def parse(cls, obj: JSONType) -> "HorizontalRule":
        cls._validate(obj)
        return cls()


HorizontalRule._e = "hr"
