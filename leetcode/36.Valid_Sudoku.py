class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(e, check):
            if "1" <= e <= "9" and e in check:
                return False
            return True
        for row in board:
            check = []
            for e in row:
                if e == '.':
                    continue
                if not is_valid(e, check):
                    return False
                check.append(e)

        for j in range(0, 9):
            check = []
            for i in range(0, 9):
                if board[i][j] == '.':
                    continue
                if not is_valid(board[i][j], check):
                    return False
                check.append(board[i][j])

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                check = []
                for p in range(3):
                    for q in range(3):
                        if board[i + p][j + q] == '.':
                            continue
                        if not is_valid(board[i + p][j + q], check):
                            return False
                        check.append(board[i + p][j + q])

        return True
