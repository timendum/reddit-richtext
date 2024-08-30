"""Reddit RichText implementation in Python"""

__version__ = "0.0.1"

from .base import FormatRange, RTDecodeError
from .document import RichTextContent
from .media import AnimatedImage, Image, Video
from .reddit import CommentLink, PostLink, SubredditLink, UserMention
from .structures import BlockQuote, Heading, List, ListElement, Paragraph
from .text import LineBreak, Link, SpoilerText, Text

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
    "Paragraph",
    "Heading",
    "ListElement",
    "List",
    "BlockQuote",
]
