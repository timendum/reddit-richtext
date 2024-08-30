import pytest

from rrichtext import RawText, RTDecodeError


def test_parsing():
    # without formatting
    e = RawText.parse({"e": "raw", "t": "Lorem"})
    assert e.text == "Lorem"


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        RawText.parse({"e": "t", "t": "Lorem"})
    # no t
    with pytest.raises(RTDecodeError):
        RawText.parse({"e": "raw", "c": "Lorem"})
    # wrong t
    with pytest.raises(RTDecodeError):
        RawText.parse({"e": "raw", "c": {}})


def test_equals():
    e = RawText.parse({"e": "raw", "t": "Lorem ipsum"})
    assert e == RawText("Lorem ipsum")


def test_inout():
    i = {"e": "raw", "t": "Lorem"}
    assert i == RawText.parse(i).to_jobj()
