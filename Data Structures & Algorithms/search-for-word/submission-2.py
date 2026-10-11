class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid(row, col):
            return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

        def dfs(visited, idx, row, col):
            if len(visited) == len(word):
                return True

            directions = [(0,1), (1,0), (0,-1), (-1, 0)]

            for direction in directions:
                next_row = row + direction[0]
                next_col = col + direction[1]
                if is_valid(next_row, next_col) and \
                (next_row, next_col) not in visited and \
                word[idx] == board[next_row][next_col]:
                    visited.add((next_row, next_col))
                    if dfs(visited, idx+1, next_row, next_col):
                        return True
                    visited.remove((next_row, next_col))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    s = set()
                    s.add((i, j))
                    if dfs(s, 1, i, j):
                        return True

        return False
