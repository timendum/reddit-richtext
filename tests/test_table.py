import pytest

from rrichtext import RTDecodeError, Table, TableCell, TableHeaderCell, TableRow, Text


def test_parsing():
    e = Table.parse(
        {
            "e": "table",
            "h": [
                {"c": [{"e": "text", "t": "a"}]},
                {"c": [{"e": "text", "t": "b"}], "a": "C"},
                {"c": [{"e": "text", "t": "c"}], "a": "R"},
                {"c": [{"e": "text", "t": "d"}], "a": "L"},
            ],
            "c": [
                [
                    {"c": [{"e": "text", "t": "a1"}]},
                    {"c": [{"e": "text", "t": "b1"}]},
                    {"c": [{"e": "text", "t": "c1"}]},
                    {"c": [{"e": "text", "t": "d1"}]},
                ],
                [
                    {"c": [{"e": "text", "t": "a+a+a"}]},
                    {"c": [{"e": "text", "t": "b+b+b"}]},
                    {"c": []},
                    {"c": []},
                ],
            ],
        }
    )
    assert len(e.headerContent) == 4
    assert len(e.rowContent) == 2
    assert len(e.rowContent[0].content) == 4
    assert e.headerContent[0].alignment is None
    assert e.headerContent[1].alignment == "C"
    assert e.headerContent[0].content[0].text == "a"  # type: ignore
    assert e.headerContent[3].content[0].text == "d"  # type: ignore


def test_parsing_errors():
    # e tag
    with pytest.raises(RTDecodeError):
        Table.parse(
            {
                "e": "text",
                "h": [
                    {"c": [{"e": "text", "t": "a"}]},
                    {"c": [{"e": "text", "t": "b"}], "a": "C"},
                    {"c": [{"e": "text", "t": "c"}], "a": "R"},
                    {"c": [{"e": "text", "t": "d"}], "a": "L"},
                ],
                "c": [
                    [
                        {"c": [{"e": "text", "t": "a1"}]},
                        {"c": [{"e": "text", "t": "b1"}]},
                        {"c": [{"e": "text", "t": "c1"}]},
                        {"c": [{"e": "text", "t": "d1"}]},
                    ],
                    [
                        {"c": [{"e": "text", "t": "a+a+a"}]},
                        {"c": [{"e": "text", "t": "b+b+b"}]},
                        {"c": []},
                        {"c": []},
                    ],
                ],
            }
        )
    # wrong h = list of str
    with pytest.raises(RTDecodeError):
        Table.parse(
            {
                "e": "text",
                "h": ["1"],
                "c": [
                    [
                        {"c": [{"e": "text", "t": "a1"}]},
                        {"c": [{"e": "text", "t": "b1"}]},
                        {"c": [{"e": "text", "t": "c1"}]},
                        {"c": [{"e": "text", "t": "d1"}]},
                    ],
                    [
                        {"c": [{"e": "text", "t": "a+a+a"}]},
                        {"c": [{"e": "text", "t": "b+b+b"}]},
                        {"c": []},
                        {"c": []},
                    ],
                ],
            }
        )
    # wrong h - wrong type
    with pytest.raises(RTDecodeError):
        Table.parse(
            {
                "e": "text",
                "h": [
                    {"e": "br"},
                    {"c": [{"e": "text", "t": "b"}], "a": "C"},
                    {"c": [{"e": "text", "t": "c"}], "a": "R"},
                    {"c": [{"e": "text", "t": "d"}], "a": "L"},
                ],
                "c": [
                    [
                        {"c": [{"e": "text", "t": "a1"}]},
                        {"c": [{"e": "text", "t": "b1"}]},
                        {"c": [{"e": "text", "t": "c1"}]},
                        {"c": [{"e": "text", "t": "d1"}]},
                    ],
                    [
                        {"c": [{"e": "text", "t": "a+a+a"}]},
                        {"c": [{"e": "text", "t": "b+b+b"}]},
                        {"c": []},
                        {"c": []},
                    ],
                ],
            }
        )
    # wrong c - wrong type
    with pytest.raises(RTDecodeError):
        Table.parse(
            {
                "e": "table",
                "h": [
                    {"c": [{"e": "text", "t": "a"}]},
                    {"c": [{"e": "text", "t": "b"}], "a": "C"},
                    {"c": [{"e": "text", "t": "c"}], "a": "R"},
                    {"c": [{"e": "text", "t": "d"}], "a": "L"},
                ],
                "c": [
                    [
                        {"c": [{"e": "text", "t": "a1"}]},
                        {"c": [{"e": "text", "t": "b1"}]},
                        {"c": [{"e": "text", "t": "c1"}]},
                        {"c": [{"e": "text", "t": "d1"}]},
                    ],
                    [
                        {"c": [{"e": "text", "t": "a+a+a"}]},
                        {"c": [{"e": "br"}]},
                        {"c": []},
                        {"c": []},
                    ],
                ],
            }
        )
    # wrong c - list of string
    with pytest.raises(RTDecodeError):
        Table.parse(
            {
                "e": "table",
                "h": [
                    {"c": [{"e": "text", "t": "a"}]},
                    {"c": [{"e": "text", "t": "b"}], "a": "C"},
                    {"c": [{"e": "text", "t": "c"}], "a": "R"},
                    {"c": [{"e": "text", "t": "d"}], "a": "L"},
                ],
                "c": [
                    [
                        {"c": [{"e": "text", "t": "a1"}]},
                        {"c": [{"e": "text", "t": "b1"}]},
                        {"c": [{"e": "text", "t": "c1"}]},
                        {"c": [{"e": "text", "t": "d1"}]},
                    ],
                    ["a2", "b2", "c2", "d2"],
                ],
            }
        )
    # wrong c - list of list of string
    with pytest.raises(RTDecodeError):
        Table.parse(
            {
                "e": "table",
                "h": [
                    {"c": [{"e": "text", "t": "a"}]},
                    {"c": [{"e": "text", "t": "b"}], "a": "C"},
                    {"c": [{"e": "text", "t": "c"}], "a": "R"},
                    {"c": [{"e": "text", "t": "d"}], "a": "L"},
                ],
                "c": [
                    [
                        {"c": [{"e": "text", "t": "a1"}]},
                        {"c": [{"e": "text", "t": "b1"}]},
                        {"c": [{"e": "text", "t": "c1"}]},
                        {"c": ["a2", "b2", "c2", "d2"]},
                    ]
                ],
            }
        )


def test_equals():
    e = Table.parse(
        {
            "e": "table",
            "h": [
                {"c": [{"e": "text", "t": "a"}]},
                {"c": [{"e": "text", "t": "b"}], "a": "C"},
                {"c": [{"e": "text", "t": "c"}], "a": "R"},
                {"c": [{"e": "text", "t": "d"}], "a": "L"},
            ],
            "c": [
                [
                    {"c": [{"e": "text", "t": "a1"}]},
                    {"c": [{"e": "text", "t": "b1"}]},
                    {"c": [{"e": "text", "t": "c1"}]},
                    {"c": [{"e": "text", "t": "d1"}]},
                ],
                [
                    {"c": [{"e": "text", "t": "a+a+a"}]},
                    {"c": [{"e": "text", "t": "b\nb"}]},
                    {"c": []},
                    {"c": []},
                ],
            ],
        }
    )
    assert e == Table(
        [
            TableHeaderCell([Text("a")]),
            TableHeaderCell([Text("b")], "C"),
            TableHeaderCell([Text("c")], "R"),
            TableHeaderCell([Text("d")], "L"),
        ],
        [
            TableRow(
                [
                    TableCell([Text("a1")]),
                    TableCell([Text("b1")]),
                    TableCell([Text("c1")]),
                    TableCell([Text("d1")]),
                ]
            ),
            TableRow(
                [
                    TableCell([Text("a+a+a")]),
                    TableCell([Text("b\nb")]),
                    TableCell([]),
                    TableCell([]),
                ]
            ),
        ],
    )


def test_inout():
    i = {
        "e": "table",
        "h": [
            {"c": [{"e": "text", "t": "a"}]},
            {"c": [{"e": "text", "t": "b"}], "a": "C"},
            {"c": [{"e": "text", "t": "c"}], "a": "R"},
            {"c": [{"e": "text", "t": "d"}], "a": "L"},
        ],
        "c": [
            [
                {"c": [{"e": "text", "t": "a1"}]},
                {"c": [{"e": "text", "t": "b1"}]},
                {"c": [{"e": "text", "t": "c1"}]},
                {"c": [{"e": "text", "t": "d1"}]},
            ],
            [
                {"c": [{"e": "text", "t": "a+a+a"}]},
                {"c": [{"e": "text", "t": "b\nb"}]},
                {"c": []},
                {"c": []},
            ],
        ],
    }
    assert i == Table.parse(i).to_jobj()


test_parsing()
