from functools import reduce
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        lower, upper = 1, max(piles)

        def canFinishBananas(k):
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            return totalTime <= h

        while lower < upper:
            mid = lower + ((upper - lower) // 2)

            if canFinishBananas(mid):
                upper = mid
            else:
                lower = mid + 1
        
        return lower

