def is_safe(board, row, col):
for i in range(row):
if board[i] == col or abs(board[i] - col) == abs(i - row):
return False
return True

def solve_nqueens(board, row):
if row == 8:
return True
for col in range(8):
if is_safe(board, row, col):
board[row] = col
if solve_nqueens(board, row + 1):
return True
board[row] = -1
return False

def print_board(board):
for row in range(8):
print(" ".join("Q" if board[row] == col else "." for col in range(8)))
print()

if name == "main":
board = [-1] * 8
print("Finding a solution for the 8-Queens problem...\n")
if solve_nqueens(board, 0):
print("Solution Board:")
print_board(board)
else:
print("No solution exists.")
