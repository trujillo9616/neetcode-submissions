class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, rows, cols = len(word), len(board), len(board[0])
        path = set()

        def dfs(row: int, col: int, i: int = 0) -> bool:
            if i == n:
                return True
            if (min(row, col) < 0 or row >= rows or col >= cols or
                board[row][col] != word[i] or
                (row, col) in path):
                return False

            path.add((row, col))
            res = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col - 1, i + 1) or
                dfs(row, col + 1, i + 1)
            )
            path.remove((row, col))
            return res

        
        for row in range(rows): 
            for col in range(cols):
                if dfs(row, col):
                    return True
        
        return False




