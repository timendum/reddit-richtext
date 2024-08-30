import pytest

from rrichtext import FormatRange, RTDecodeError


def test_parsing_basic():
    e = FormatRange.parse([0, 0, 12])
    assert e.f == 0
    assert e.t == 12
    # error
    with pytest.raises(RTDecodeError):
        FormatRange.parse([0, 0])
    with pytest.raises(RTDecodeError):
        FormatRange.parse([0, 0, "x"])


def test_parsing_formattingFlag():
    e = FormatRange.parse([0, 0, 12])
    assert e.bold == False
    assert e.italic == False
    assert e.underline == False
    assert e.strikethrough == False
    assert e.subscript == False
    assert e.superscript == False
    assert e.monospace == False
    # all
    e = FormatRange.parse([127, 0, 2])
    assert e.bold == True
    assert e.italic == True
    assert e.underline == True
    assert e.strikethrough == True
    assert e.subscript == True
    assert e.superscript == True
    assert e.monospace == True
    # mixed
    e = FormatRange.parse([19, 0, 2])
    assert e.bold == True
    assert e.italic == True
    assert e.underline == False
    assert e.strikethrough == False
    assert e.subscript == True
    assert e.superscript == False
    assert e.monospace == False
    # mixed 2
    e = FormatRange.parse([108, 0, 2])
    assert e.bold == False
    assert e.italic == False
    assert e.underline == True
    assert e.strikethrough == True
    assert e.subscript == False
    assert e.superscript == True
    assert e.monospace == True


def test_equals():
    e = FormatRange.parse([0, 3, 11])
    assert e == FormatRange(3, 11)


def test_inout():
    i = [6, 7, 121]
    e = FormatRange.parse(i)
    assert e.to_jobj() == i
