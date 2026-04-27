class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = top + ((bot - top) // 2)
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l, r = 0, COLS - 1
        row = top + ((bot - top) // 2)
        while l <= r:
            m = l + ((r - l) // 2)
            currentNum = matrix[row][m]
            if target == currentNum:
                return True
            
            elif target > currentNum:
                l = m + 1
            else:
                r = m - 1
        return False