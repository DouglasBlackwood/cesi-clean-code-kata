import dataclasses

EMPTY_CELL = 0


def is_solved(board_content):
    return Board(board_content).winner()


@dataclasses.dataclass
class Board:
    board: list[list[int]]

    DRAW = 0
    UNFINISHED = -1
    PLAYER_1 = 1
    PLAYER_2 = 2

    def row(self, i):
        return Line(self.board[i])

    def column(self, i):
        return Line([self.board[0][i], self.board[1][i], self.board[2][i]])

    def diagonal1(self):
        return Line([self.board[0][0], self.board[1][1], self.board[2][2]])

    def diagonal2(self):
        return Line([self.board[0][2], self.board[1][1], self.board[2][0]])

    def is_finished(self):
        return (
            self.row(0).is_finished()
            and self.row(1).is_finished()
            and self.row(2).is_finished()
        )

    def winner(self):
        for i in range(0, 3):
            if self.row(i).is_solved():
                return self.row(i).first_cell()
            if self.column(i).is_solved():
                return self.column(i).first_cell()

        if self.diagonal1().is_solved():
            return self.diagonal1().first_cell()
        if self.diagonal2().is_solved():
            return self.diagonal2().first_cell()

        if self.is_finished():
            return self.DRAW

        return self.UNFINISHED


@dataclasses.dataclass
class Line:
    cells: list[int]

    def is_solved(self):
        return self.cells[0] == self.cells[1] == self.cells[2] != EMPTY_CELL

    def first_cell(self):
        return self.cells[0]

    def is_finished(self):
        return EMPTY_CELL not in self.cells
