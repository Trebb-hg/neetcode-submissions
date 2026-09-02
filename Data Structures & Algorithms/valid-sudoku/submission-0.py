class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        boxes=collections.defaultdict(set)
        for i in range(9):
            for o in range(9):
                if board[i][o]==".":
                    continue
                if board[i][o] in rows[i] or board[i][o] in cols[o] or board[i][o] in boxes[(i//3,o//3)]:
                    return False
                rows[i].add(board[i][o])
                cols[o].add(board[i][o])
                boxes[(i//3,o//3)].add(board[i][o])
        return True        