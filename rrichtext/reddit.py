from dataclasses import dataclass

from .base import JSONType, _ElementNode


@dataclass
class CommentLink(_ElementNode):
    text: str

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "t": self.text}

    @classmethod
    def parse(cls, obj: JSONType) -> "CommentLink":
        cls._validate(obj)
        return cls(cls._get_jobj_value(obj, ("t",), str))


CommentLink._e = "c/"


@dataclass
class PostLink(_ElementNode):
    permalink: str

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "t": self.permalink}

    @classmethod
    def parse(cls, obj: JSONType) -> "PostLink":
        cls._validate(obj)
        return cls(cls._get_jobj_value(obj, ("t",), str))


PostLink._e = "p/"


@dataclass
class SubredditLink(_ElementNode):
    subredditName: str
    showPrefix: bool

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "t": self.subredditName, "l": self.showPrefix}

    @classmethod
    def parse(cls, obj: JSONType) -> "SubredditLink":
        cls._validate(obj)
        return cls(
            cls._get_jobj_value(obj, ("t",), str), cls._get_jobj_value(obj, ("l",), bool, True)
        )


SubredditLink._e = "r/"


@dataclass
class UserLink(_ElementNode):
    username: str
    showPrefix: bool

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "t": self.username, "l": self.showPrefix}

    @classmethod
    def parse(cls, obj: JSONType) -> "UserLink":
        cls._validate(obj)
        return cls(cls._get_jobj_value(obj, ("t",), str), cls._get_jobj_value(obj, ("l",), bool))


UserLink._e = "u"


@dataclass
class UserMention(_ElementNode):
    username: str
    showPrefix: bool

    def to_jobj(self) -> JSONType:
        return {"e": self._e, "t": self.username, "l": self.showPrefix}

    @classmethod
    def parse(cls, obj: JSONType) -> "UserMention":
        cls._validate(obj)
        return cls(cls._get_jobj_value(obj, ("t",), str), cls._get_jobj_value(obj, ("l",), bool))


UserMention._e = "@"

_RedditLink = CommentLink | PostLink | SubredditLink | UserLink | UserMention
