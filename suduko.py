Approximately 5x faster using pruning:

def is_valid_board(board, i, j, n):
    for idx in range(9):
        if n == board[i][idx] \
            or n == board[idx][j] \
            or n == board[(i - i % 3) + idx // 3][(j - j % 3) + idx % 3]:
            return False
        
    return True


def get_candidates(board, i, j):
    return [n for n in map(str, range(1, 10)) if is_valid_board(board, i, j, n)]


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ii, jj, candidates = None, None, None
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    new_candidates = get_candidates(board, i, j)
                    if candidates is None or 0 < len(new_candidates) < len(candidates):
                        candidates = new_candidates
                        ii, jj = i, j

        if candidates is None:
            # board is complete
            return True
        
        for c in candidates:
            board[ii][jj] = c
            if self.solveSudoku(board):
                return True
            board[ii][jj] = '.'  # backtrack
        
        # no valid candidate
        return False
