import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, row, N):
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_queens(board, row + 1, N)
            board[row][col] = 0

def print_solution(board):
    N = len(board)
    solution = []
    for i in range(N):
        row = ""
        for j in range(N):
            if board[i][j] == 1:
                row += "Q "
            else:
                row += ". "
        solution.append(row.strip())
    print(", ".join(solution))

def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_queens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    nqueens(sys.argv[1])

