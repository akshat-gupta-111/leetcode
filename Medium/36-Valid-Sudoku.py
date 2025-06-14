'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

https://leetcode.com/problems/valid-sudoku/description/

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_ = defaultdict(set)
        col_ = defaultdict(set)
        square = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in row_[row]) or (board[row][col] in col_[col]) or (board[row][col] in square[(row//3,col//3)]):
                    return False
                
                row_[row].add(board[row][col])
                col_[col].add(board[row][col])
                square[(row // 3, col //3)].add(board[row][col])
        
        return True   
            

                
        