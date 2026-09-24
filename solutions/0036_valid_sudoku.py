"""
LeetCode 36 — Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to
be validated according to the following rules:
- Each row must contain digits 1-9 without duplicates
- Each column must contain digits 1-9 without duplicates
- Each of the nine 3x3 sub-boxes must contain digits 1-9 without duplicates

Example:
    Input:  [["5","3",".",".","7",".",".",".","."], ...]
    Output: true

Approach: Three passes with sets for rows, cols, boxes.
Time:  O(81) = O(1)
Space: O(81) = O(1)
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                box_idx = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        return True


if __name__ == "__main__":
    s = Solution()
    valid = [
        [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]],
    ]
    invalid = [
        [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]],
    ]
    for board in valid:
        assert s.isValidSudoku(board) is True
        print("OK valid board")
    for board in invalid:
        assert s.isValidSudoku(board) is False
        print("OK invalid board")
