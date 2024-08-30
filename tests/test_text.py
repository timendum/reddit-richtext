import pytest

from rrichtext import FormatRange, RTDecodeError, Text


def test_parsing():
    # without formatting
    e = Text.parse({"e": "text", "t": "content"})
    assert e.text == "content"
    assert not e.formattings
    # with formatting
    e = Text.parse({"e": "text", "t": "content", "f": [[0, 0, 4]]})
    assert e.text == "content"
    assert e.formattings


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        Text.parse({"e": "t", "t": "content"})
    with pytest.raises(RTDecodeError):
        Text.parse({"e": "text", "t": 0})


def test_equals():
    e = Text.parse({"e": "text", "t": "content"})
    assert e == Text("content")
    e = Text.parse({"e": "text", "t": "content", "f": [[0, 0, 4]]})
    assert e == Text("content", [FormatRange(0, 4)])


def test_inout():
    i = {"e": "text", "t": "content"}
    assert i == Text.parse(i).to_jobj()
    i = {"e": "text", "t": "content", "f": [[1, 0, 3]]}
    assert i == Text.parse(i).to_jobj()


def test_fill_text():
    e = Text("text content")
    FormatRange.fill_text(e)
    assert e.formattings
    assert e.formattings[0].to_jobj() == [0, 0, len(e.text)]
