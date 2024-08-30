import pytest

from rrichtext import Image, RTDecodeError


def test_parsing():
    e = Image.parse({"e": "img", "id": "we3lktrj"})
    assert e.id == "we3lktrj"
    e = Image.parse({"e": "img", "id": "f19i0mluc1", "c": "Text caption", "o": "blurred"})
    assert e.caption == "Text caption"
    assert e.blur == "blurred"


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        Image.parse({"e": "t", "id": "we3lktrj"})
    # missing id
    with pytest.raises(RTDecodeError):
        Image.parse({"e": "img"})


def test_equals():
    e = Image.parse({"e": "img", "id": "f19i0mluc1", "c": "Text caption", "o": "blurred"})
    assert e == Image("f19i0mluc1", "Text caption", "blurred")


def test_inout():
    i = {"e": "img", "id": "f19i0mluc1", "c": "Text caption", "o": "blurred"}
    assert i == Image.parse(i).to_jobj()
    i = {
        "e": "img",
        "id": "f19i0mluc1",
    }
    assert i == Image.parse(i).to_jobj()
