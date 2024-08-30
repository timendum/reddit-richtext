import pytest

from rrichtext import Heading, RawText, RTDecodeError


def test_parsing():
    # without formatting
    e = Heading.parse({"e": "h", "l": 1, "c": [{"e": "raw", "t": "Doloret"}]})
    assert e.level == 1
    assert len(e.content) == 1


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        Heading.parse({"e": "l", "l": 1, "c": [{"e": "raw", "t": "Doloret"}]})
    # no l
    with pytest.raises(RTDecodeError):
        Heading.parse({"e": "h", "c": [{"e": "raw", "t": "Doloret"}]})
    # wrong l
    with pytest.raises(RTDecodeError):
        Heading.parse({"e": "h", "l": "1", "c": [{"e": "raw", "t": "Doloret"}]})
    # no c
    with pytest.raises(RTDecodeError):
        Heading.parse({"e": "h", "l": 1})
    # wrong c type
    with pytest.raises(RTDecodeError):
        Heading.parse({"e": "h", "l": 1, "c": "Doloret"})
    # wrong c subtype
    with pytest.raises(RTDecodeError):
        Heading.parse(
            {"e": "h", "l": 1, "c": [{"e": "h", "l": 1, "c": [{"e": "raw", "t": "Doloret"}]}]}
        )


def test_equals():
    e = Heading.parse({"e": "h", "l": 3, "c": [{"e": "raw", "t": "Doloret"}]})
    assert e == Heading(level=3, content=[RawText("Doloret")])


def test_inout():
    i = {"e": "h", "l": 2, "c": [{"e": "raw", "t": "Doloret"}]}
    assert i == Heading.parse(i).to_jobj()
