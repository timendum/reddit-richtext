import pytest

from rrichtext import HorizontalRule, RTDecodeError


def test_parsing():
    e = HorizontalRule.parse({"e": "hr"})
    assert e


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        HorizontalRule.parse({"e": "br"})


def test_equals():
    e = HorizontalRule.parse({"e": "hr"})
    assert e == HorizontalRule()


def test_inout():
    i = {"e": "hr"}
    assert i == HorizontalRule.parse(i).to_jobj()
