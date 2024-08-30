import pytest

from rrichtext import FormatRange, Link, RTDecodeError


def test_parsing():
    # basic
    e = Link.parse({"e": "link", "t": "image", "u": "https://i.imgur.com/Q0s0ntP.jpg"})
    assert e.text == "image"
    assert not e.formattings
    assert e.url == "https://i.imgur.com/Q0s0ntP.jpg"
    # with tooltip
    e = Link.parse(
        {"e": "link", "t": "image", "u": "https://i.imgur.com/Q0s0ntP.jpg", "a": "alt text"}
    )
    assert e.tooltip == "alt text"
    # with formatting
    e = Link.parse(
        {"e": "link", "t": "image", "u": "https://i.imgur.com/Q0s0ntP.jpg", "f": [[0, 0, 12]]}
    )
    assert e.text
    assert e.formattings


def test_parsing_errors():
    with pytest.raises(RTDecodeError):
        Link.parse({"e": "text", "t": "content"})
    with pytest.raises(RTDecodeError):
        Link.parse({"e": "link", "u": "u"})
    with pytest.raises(RTDecodeError):
        Link.parse({"e": "link", "t": "u"})
    with pytest.raises(RTDecodeError):
        Link.parse({"e": "link", "t": 0, "u": "u"})
    with pytest.raises(RTDecodeError):
        Link.parse({"e": "link", "t": "t", "u": [0]})
    with pytest.raises(RTDecodeError):
        Link.parse({"e": "link"})
    with pytest.raises(RTDecodeError):
        Link.parse({"e": "link", "t": "t", "u": "u", "a": 0})


def test_equals():
    e = Link.parse({"e": "link", "t": "content", "u": "url"})
    assert e == Link("content", "url")
    e = Link.parse({"e": "link", "t": "content", "u": "url", "f": [[0, 0, 4]]})
    assert e == Link("content", "url", [FormatRange(0, 4)])


def test_inout():
    i = {"e": "link", "t": "content", "u": "url"}
    assert i == Link.parse(i).to_jobj()
    i = {"e": "link", "t": "content", "u": "url", "a": "tooltip", "f": [[1, 0, 3]]}
    assert i == Link.parse(i).to_jobj()


def test_fill_text():
    e = Link("content", "url")
    FormatRange.fill_text(e)
    assert e.formattings
    assert e.formattings[0].to_jobj() == [0, 0, len(e.text)]
