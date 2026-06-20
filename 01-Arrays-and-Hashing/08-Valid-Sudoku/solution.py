"""
Problem: Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/
Approach: One-pass Hash Map validation. Track seen numbers in rows, columns, 
and 3x3 squares. Map squares using integer division: (r // 3, c // 3).
Time Complexity: O(1) - Fixed 9x9 board
Space Complexity: O(1) - Fixed 9x9 board
"""
from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dictionary of sets to track seen numbers
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # Key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # If the value is already in the current row, col, or square, it's invalid
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                
                # Otherwise, add it to our tracking sets
                cols[c].add(val)
                rows[r].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True