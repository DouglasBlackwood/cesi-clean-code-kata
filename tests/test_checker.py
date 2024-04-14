import pytest

from tictactoe_checker import checker


@pytest.mark.parametrize(
    ("board", "expected"),
    (
        (
            [
                [1, 1, 1],
                [0, 2, 2],
                [0, 0, 0],
            ],
            1,
        ),
        (
            [
                [1, 2, 0],
                [0, 1, 2],
                [0, 0, 1],
            ],
            1,
        ),
        (
            [
                [0, 2, 1],
                [0, 1, 2],
                [1, 0, 0],
            ],
            1,
        ),
        (
            [
                [2, 1, 1],
                [0, 1, 1],
                [2, 2, 2],
            ],
            2,
        ),
        (
            [
                [2, 2, 2],
                [0, 1, 1],
                [1, 0, 0],
            ],
            2,
        ),
        (
            [
                [2, 1, 1],
                [2, 1, 1],
                [2, 0, 0],
            ],
            2,
        ),
        (
            [
                [2, 1, 2],
                [2, 1, 1],
                [1, 2, 1],
            ],
            0,
        ),
        (
            [
                [1, 2, 1],
                [1, 1, 2],
                [2, 1, 2],
            ],
            0,
        ),
        (
            [
                [2, 0, 2],
                [2, 1, 1],
                [1, 2, 1],
            ],
            -1,
        ),
        (
            [
                [0, 0, 2],
                [0, 0, 0],
                [1, 0, 1],
            ],
            -1,
        ),
        (
            [
                [1, 2, 1],
                [1, 1, 2],
                [2, 2, 0],
            ],
            -1,
        ),
        (
            [
                [0, 1, 1],
                [2, 0, 2],
                [2, 1, 0],
            ],
            -1,
        ),
    ),
)
def test_checker(board, expected):
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
    assert checker.is_solved(board) == expected
