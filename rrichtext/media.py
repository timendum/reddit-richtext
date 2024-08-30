from dataclasses import dataclass

from .base import JSONType, _ElementNode


@dataclass
class Image(_ElementNode):
    id: str
    caption: None | str = None
    blur: None | str = None

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"e": self._e, "id": self.id}
        if self.caption:
            r["c"] = self.caption
        if self.blur:
            r["o"] = self.blur
        return r

    @classmethod
    def parse(cls, obj: JSONType) -> "Image":
        cls._validate(obj)
        return cls(
            cls._get_jobj_value(obj, "id", str),
            cls._get_jobj_value(obj, "c", str, True),
            cls._get_jobj_value(obj, "o", str, True),
        )


Image._e = "img"


@dataclass
class AnimatedImage(_ElementNode):
    id: str
    caption: None | str = None
    blur: None | str = None

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"e": self._e, "id": self.id}
        if self.caption:
            r["c"] = self.caption
        if self.blur:
            r["o"] = self.blur
        return r

    @classmethod
    def parse(cls, obj: JSONType) -> "AnimatedImage":
        cls._validate(obj)
        return cls(
            cls._get_jobj_value(obj, "id", str),
            cls._get_jobj_value(obj, "c", str, True),
            cls._get_jobj_value(obj, "o", str, True),
        )


AnimatedImage._e = "gif"


@dataclass
class Video(_ElementNode):
    id: str
    caption: None | str = None
    blur: None | str = None
    thumbnail: None | Image = None
    convertToGif: None | bool = None

    def to_jobj(self) -> JSONType:
        r: dict[str, JSONType] = {"e": self._e, "id": self.id}
        if self.caption:
            r["c"] = self.caption
        if self.blur:
            r["o"] = self.blur
        if self.thumbnail:
            r["p"] = self.thumbnail.to_jobj()
        if self.convertToGif:
            r["gifify"] = self.convertToGif
        return r

    @classmethod
    def parse(cls, obj: JSONType):
        cls._validate(obj)
        p = cls._get_jobj_value(obj, "p", dict, True)
        return cls(
            cls._get_jobj_value(obj, "id", str),
            cls._get_jobj_value(obj, "c", str, True),
            cls._get_jobj_value(obj, "o", str, True),
            Image.parse(p) if p else None,
            cls._get_jobj_value(obj, "convertToGif", bool, True),
        )


Video._e = "video"


_Media = Image | AnimatedImage | Video
