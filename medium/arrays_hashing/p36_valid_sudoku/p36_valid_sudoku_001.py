from collections import defaultdict


class Solution:
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:

        row_set = defaultdict(set)
        column_set = defaultdict(set)
        square_set = defaultdict(set)  # r //3; c //3

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in row_set[r] or
                      board[r][c] in column_set[c] or
                      board[r][c] in square_set[(r // 3, c // 3)]):
                    return False

                row_set[r].add(board[r][c])
                column_set[c].add(board[r][c])
                square_set[(r // 3, c // 3)].add(board[r][c])

        return True
