import pytest

from rrichtext import BlockQuote, Paragraph, RTDecodeError, Text


def test_parsing():
    # basic
    e = BlockQuote.parse(
        {"e": "blockquote", "c": [{"e": "par", "c": [{"e": "text", "t": "lorem"}]}]}
    )
    assert len(e.content) == 1
    # basic
    e = BlockQuote.parse(
        {
            "e": "blockquote",
            "c": [{"e": "par", "c": [{"e": "text", "t": "lorem"}]}],
            "a": {"e": "text", "t": "ipsum"},
        }
    )
    assert len(e.content) == 1
    assert e.author.text == "ipsum"


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        BlockQuote.parse(
            {"e": "text", "c": [{"e": "par", "c": [{"e": "text", "t": "lorem", "f": [[0, 0, 9]]}]}]}
        )
    # missing c
    with pytest.raises(RTDecodeError):
        BlockQuote.parse({"e": "blockquote", "u": "u"})
    # wrong c
    with pytest.raises(RTDecodeError):
        BlockQuote.parse({"e": "text", "c": "par"})
    # wrong a
    with pytest.raises(RTDecodeError):
        BlockQuote.parse(
            {"e": "text", "c": [{"e": "par", "c": [{"e": "text", "t": "lorem"}], "a": "ipsum"}]}
        )


def test_equals():
    e = BlockQuote.parse(
        {"e": "blockquote", "c": [{"e": "par", "c": [{"e": "text", "t": "lorem"}]}]}
    )
    assert e == BlockQuote([Paragraph([Text("lorem")])])


def test_inout():
    i = {"e": "blockquote", "c": [{"e": "par", "c": [{"e": "text", "t": "lorem"}]}]}
    assert i == BlockQuote.parse(i).to_jobj()
