import pytest

from rrichtext import AnimatedImage, RTDecodeError


def test_parsing():
    e = AnimatedImage.parse({"e": "gif", "id": "we3lktrj"})
    assert e.id == "we3lktrj"
    e = AnimatedImage.parse({"e": "gif", "id": "f19i0mluc1", "c": "Text caption", "o": "blurred"})
    assert e.caption == "Text caption"
    assert e.blur == "blurred"


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        AnimatedImage.parse({"e": "t", "id": "we3lktrj"})
    # missing id
    with pytest.raises(RTDecodeError):
        AnimatedImage.parse({"e": "gif"})


def test_equals():
    e = AnimatedImage.parse({"e": "gif", "id": "f19i0mluc1", "c": "Text caption", "o": "blurred"})
    assert e == AnimatedImage("f19i0mluc1", "Text caption", "blurred")


def test_inout():
    i = {"e": "gif", "id": "f19i0mluc1", "c": "Text caption", "o": "blurred"}
    assert i == AnimatedImage.parse(i).to_jobj()
    i = {
        "e": "gif",
        "id": "f19i0mluc1",
    }
    assert i == AnimatedImage.parse(i).to_jobj()
