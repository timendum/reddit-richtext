"""Reddit RichText implementation in Python"""

__version__ = "0.0.1"

from .base import FormatRange, HorizontalRule, LineBreak, RTDecodeError
from .document import RichTextContent
from .media import AnimatedImage, Image, Video
from .reddit import CommentLink, PostLink, SubredditLink, UserMention
from .structures import (
    BlockQuote,
    CodeBlock,
    Heading,
    List,
    ListElement,
    Paragraph,
    Table,
    TableCell,
    TableHeaderCell,
    TableRow,
)
from .text import Link, RawText, SpoilerText, Text

__all__ = [
    "FormatRange",
    "RTDecodeError",
    "RichTextContent",
    "AnimatedImage",
    "Image",
    "Video",
    "CommentLink",
    "PostLink",
    "SubredditLink",
    "UserMention",
    "LineBreak",
    "Link",
    "SpoilerText",
    "Text",
    "RawText",
    "Paragraph",
    "Heading",
    "ListElement",
    "List",
    "BlockQuote",
    "CodeBlock",
    "Table",
    "TableCell",
    "TableHeaderCell",
    "TableRow",
    "HorizontalRule",
]


try:
    from . import rpraw  # noqa: F401

    __all__.append("rpraw")
except ImportError:
    pass
