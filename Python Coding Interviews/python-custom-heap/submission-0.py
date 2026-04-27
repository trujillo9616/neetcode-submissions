from heapq import heappush, heappop
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []

    for n in nums:
        heappush(max_heap, (-n, n))
    
    res = []
    while max_heap:
        res.append(heappop(max_heap)[1])
    
    return res



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
