class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # 1. Find the correct row
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = top + ((bot - top) // 2)

            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        if not top <= bot:
            return False

        # 2. Find the element in the row
        L, R = 0, COLS - 1
        row = top + ((bot - top) // 2)

        while L <= R:
            col = L + ((R - L) // 2)
            currentNum = matrix[row][col]

            if target == currentNum:
                return True
            
            if target > currentNum:
                L = col + 1
            else:
                R = col - 1
        return False