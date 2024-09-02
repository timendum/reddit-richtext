"""Reddit RichText implementation in Python"""

__version__ = "0.0.1"

from .base import FormatRange, RTDecodeError
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
from .text import LineBreak, Link, RawText, SpoilerText, Text

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
]
