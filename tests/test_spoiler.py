import pytest

from rrichtext import Link, RTDecodeError, SpoilerText, Text


def test_parsing():
    # without formatting
    e = SpoilerText.parse(
        {
            "e": "spoilertext",
            "c": [
                {"e": "text", "t": "spoiler ", "f": [[0, 0, 7]]},
                {"e": "link", "t": "url", "u": "https://redd.it", "f": [[0, 0, 3]]},
            ],
        }
    )
    assert e.content
    assert len(e.content) == 2
    assert hasattr(e.content[0], "text") and e.content[0].text == "spoiler "  # type: ignore
    assert hasattr(e.content[1], "text") and e.content[1].text == "url"  # type: ignore
    assert e.content[1]._e == "link"


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        SpoilerText.parse({"e": "t", "c": []})
    # no c
    with pytest.raises(RTDecodeError):
        SpoilerText.parse({"e": "spoilertext", "t": 0})
    # wrong c
    with pytest.raises(RTDecodeError):
        SpoilerText.parse({"e": "spoilertext", "c": [0, "a"]})
    # wrong c
    with pytest.raises(RTDecodeError):
        SpoilerText.parse(
            {"e": "spoilertext", "c": [{"e": "spoilertext", "c": [{"e": "text", "t": "spoiler "}]}]}
        )


def test_equals():
    e = SpoilerText.parse(
        {
            "e": "spoilertext",
            "c": [
                {"e": "text", "t": "spoiler "},
                {"e": "link", "t": "url", "u": "https://redd.it"},
            ],
        }
    )
    assert e == SpoilerText([Text("spoiler "), Link("url", "https://redd.it")])


def test_inout():
    i = {
        "e": "spoilertext",
        "c": [
            {"e": "text", "t": "spoiler ", "f": [[0, 0, 7]]},
            {"e": "link", "t": "url", "u": "https://redd.it", "f": [[0, 0, 3]]},
        ],
    }
    assert i == SpoilerText.parse(i).to_jobj()
