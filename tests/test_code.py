import pytest

from rrichtext import CodeBlock, RawText, RTDecodeError


def test_parsing():
    e = CodeBlock.parse({"e": "code", "c": [{"e": "raw", "t": "lorem"}]})
    assert len(e.content) == 1
    assert hasattr(e.content[0], "text") and e.content[0].text == "lorem"  # type: ignore
    e = CodeBlock.parse(
        {
            "e": "code",
            "c": [
                {"e": "raw", "t": "lorem"},
                {"e": "raw", "t": "ipsum?"},
                {"e": "raw", "t": "temet lorus "},
            ],
            "l": " java",
        }
    )
    assert len(e.content) == 3
    assert e.language == " java"
    assert hasattr(e.content[2], "text") and e.content[2].text == "temet lorus "  # type: ignore


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        e = CodeBlock.parse({"e": "t", "c": [{"e": "raw", "t": "lorem"}]})
    # no c
    with pytest.raises(RTDecodeError):
        CodeBlock.parse({"e": "code", "t": 0})
    # wrong c
    with pytest.raises(RTDecodeError):
        CodeBlock.parse({"e": "t", "c": ["lorem"]})
    # wrong l
    with pytest.raises(RTDecodeError):
        CodeBlock.parse(
            {
                "e": "code",
                "c": [
                    {"e": "raw", "t": "lorem"},
                    {"e": "raw", "t": "ipsum?"},
                    {"e": "raw", "t": "temet lorus "},
                ],
                "l": 1,
            }
        )


def test_equals():
    e = CodeBlock.parse(
        {
            "e": "code",
            "c": [
                {"e": "raw", "t": "lorem"},
                {"e": "raw", "t": "ipsum?"},
                {"e": "raw", "t": "temet\nlorus "},
            ],
            "l": " java",
        }
    )
    assert e == CodeBlock([RawText("lorem"), RawText("ipsum?"), RawText("temet\nlorus ")], " java")


def test_inout():
    i = {
        "e": "code",
        "c": [
            {"e": "raw", "t": "lorem"},
            {"e": "raw", "t": "ipsum?"},
            {"e": "raw", "t": "temet\nlorus "},
        ],
        "l": " java",
    }
    assert i == CodeBlock.parse(i).to_jobj()
