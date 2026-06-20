import pytest
from solution import Solution

class TestValidSudoku:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    # Base valid board from LeetCode Example 1
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    def test_valid_sudoku_standard(self):
        assert self.solver.isValidSudoku(self.valid_board) == True

    def test_invalid_sudoku_row_duplicate(self):
        # Create a deep copy and force a row duplicate
        board = [row[:] for row in self.valid_board]
        board[0][8] = "5" # '5' already exists at board[0][0]
        assert self.solver.isValidSudoku(board) == False

    def test_invalid_sudoku_col_duplicate(self):
        board = [row[:] for row in self.valid_board]
        board[8][0] = "5" # '5' already exists at board[0][0]
        assert self.solver.isValidSudoku(board) == False

    def test_invalid_sudoku_square_duplicate(self):
        board = [row[:] for row in self.valid_board]
        # Top-left 3x3 square already has a '5' at [0][0]. 
        # We put another '5' at [2][2] (same 3x3 square, different row/col)
        board[2][2] = "5" 
        assert self.solver.isValidSudoku(board) == False

    def test_empty_board(self):
        # A completely empty board is technically valid per the rules
        empty_board = [["." for _ in range(9)] for _ in range(9)]
        assert self.solver.isValidSudoku(empty_board) == True

    def test_full_valid_board(self):
        # A completely solved, valid Sudoku board
        full_board = [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","9"]
        ]
        assert self.solver.isValidSudoku(full_board) == True
        
    def test_full_invalid_board(self):
        # Take the full valid board and ruin the very last element
        full_board = [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","8"] # Changed '9' to '8'
        ]
        assert self.solver.isValidSudoku(full_board) == False