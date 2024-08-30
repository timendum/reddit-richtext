import pytest

from rrichtext import RTDecodeError, SubredditLink


def test_parsing():
    # without showPrefix
    e = SubredditLink.parse({"e": "r/", "t": "all"})
    assert e.subredditName == "all"
    e = SubredditLink.parse({"e": "r/", "t": "pics", "l": True})
    assert e.subredditName == "pics"
    assert e.showPrefix is True


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        SubredditLink.parse({"e": "t", "t": "all"})
    # missing t
    with pytest.raises(RTDecodeError):
        SubredditLink.parse({"e": "r/", "l": True})
    # wrong t
    with pytest.raises(RTDecodeError):
        SubredditLink.parse({"e": "r/", "t": True})


def test_equals():
    e = SubredditLink.parse({"e": "r/", "t": "all", "l": True})
    assert e == SubredditLink("all", True)


def test_inout():
    i = {"e": "r/", "t": "all", "l": True}
    assert i == SubredditLink.parse(i).to_jobj()
