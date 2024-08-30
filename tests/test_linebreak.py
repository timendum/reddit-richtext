import pytest

from rrichtext import FormatRange, LineBreak, RTDecodeError


def test_parsing():
    # without formatting
    e = LineBreak.parse({"e": "br"})
    assert e


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        LineBreak.parse({"e": "t", "t": "content"})


def test_equals():
    e = LineBreak.parse({"e": "br"})
    assert e == LineBreak()


def test_inout():
    i = {"e": "br"}
    assert i == LineBreak.parse(i).to_jobj()


def test_fill_text():
    e = LineBreak()
    with pytest.raises(ValueError):
        FormatRange.fill_text(e, "_e")
