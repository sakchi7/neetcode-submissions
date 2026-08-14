class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        sq = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if i not in row:
                        row[i] = [board[i][j]]
                    else:
                        if board[i][j] in row[i]:
                            return False
                        row[i].append(board[i][j])
                    if j not in col:
                        col[j] = [board[i][j]]
                    else:
                        if board[i][j] in col[j]:
                            return False
                        col[j].append(board[i][j])

        
                    sqind = int((i//3)*3+(j//3))
                    if sqind not in sq:
                        sq[sqind] = [board[i][j]]
                    else:
                        if board[i][j] in sq[sqind]:
                            return False
                        sq[sqind].append(board[i][j])
        return True