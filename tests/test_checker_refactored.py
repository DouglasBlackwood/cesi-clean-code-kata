import pytest

from tictactoe_checker import checker_refactored as checker


@pytest.mark.parametrize(
    ("board", "expected"),
    (
        (
            [
                [1, 1, 1],
                [0, 2, 2],
                [0, 0, 0],
            ],
            checker.Board.PLAYER_1,
        ),
        (
            [
                [1, 2, 0],
                [0, 1, 2],
                [0, 0, 1],
            ],
            checker.Board.PLAYER_1,
        ),
        (
            [
                [0, 2, 1],
                [0, 1, 2],
                [1, 0, 0],
            ],
            checker.Board.PLAYER_1,
        ),
        (
            [
                [2, 1, 1],
                [0, 1, 1],
                [2, 2, 2],
            ],
            checker.Board.PLAYER_2,
        ),
        (
            [
                [2, 2, 2],
                [0, 1, 1],
                [1, 0, 0],
            ],
            checker.Board.PLAYER_2,
        ),
        (
            [
                [2, 1, 1],
                [2, 1, 1],
                [2, 0, 0],
            ],
            checker.Board.PLAYER_2,
        ),
        (
            [
                [2, 1, 2],
                [2, 1, 1],
                [1, 2, 1],
            ],
            checker.Board.DRAW,
        ),
        (
            [
                [1, 2, 1],
                [1, 1, 2],
                [2, 1, 2],
            ],
            checker.Board.DRAW,
        ),
        (
            [
                [2, 0, 2],
                [2, 1, 1],
                [1, 2, 1],
            ],
            checker.Board.UNFINISHED,
        ),
        (
            [
                [0, 0, 2],
                [0, 0, 0],
                [1, 0, 1],
            ],
            checker.Board.UNFINISHED,
        ),
        (
            [
                [1, 2, 1],
                [1, 1, 2],
                [2, 2, 0],
            ],
            checker.Board.UNFINISHED,
        ),
        (
            [
                [0, 1, 1],
                [2, 0, 2],
                [2, 1, 0],
            ],
            checker.Board.UNFINISHED,
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
