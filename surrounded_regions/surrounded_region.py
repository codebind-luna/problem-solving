from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        safe = set()
        seen = set()
        n, m = len(board), len(board[0])
        stack = [(i, j) for i in (0, n - 1) for j in range(1, m - 1)] + [(i, j) for j in (0, m - 1) for i in range(n)]
        
        while stack:
            i, j = stack.pop()
            if (i, j) not in seen and board[i][j] == 'O':
                safe.add((i, j))
                if i > 0:
                    stack.append((i - 1, j))
                if i < n - 1:
                    stack.append((i + 1, j))
                if j > 0:
                    stack.append((i, j - 1))
                if j < m - 1:
                    stack.append((i, j + 1))
            seen.add((i, j))
            
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == 'O' and (i, j) not in safe:
                    board[i][j] = 'X'
