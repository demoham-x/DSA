def isValid(board, row, col, n):
    # initializing temporary column variable
    temp_col = col
    # checking each column of a row for queens
    while temp_col >= 0:
        if board[row][temp_col] == 1:
            return False
        temp_col -= 1
    
    # reinitializing temporary row and column variable
    temp_row = row
    temp_col = col
    # checking top-left diagonal for queens
    while temp_row >= 0 and temp_col >= 0:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row -= 1
        temp_col -= 1
    
    # reinitilizing temporary row and column variable
    temp_row = row
    temp_col = col
    # checking bottom-left diagonal for queens
    while temp_row < n and temp_col >= 0:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row += 1
        temp_col -= 1
    
    # if no queen is found, the position is valid and returning True
    return True


def solve(board, n, col, ans):
    # base case - reached the end of the board
    if col == n:
        string = ""
        for row in board:
            for val in row:
                string += str(val)
        ans.append(string)
        return

    # looping through row
    for row in range(n):
        # if the position is valid, queen is placed and moved to
        # next column
        if isValid(board, row, col, n):
            board[row][col] = 1
            solve(board, n, col + 1, ans)

            # backtrack - queen is removed and looked for next possibility
            board[row][col] = 0


def nQueens(n):
    ans = []
    # empty board
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, n, 0, ans)
    # finally returning all possible placements
    return ans