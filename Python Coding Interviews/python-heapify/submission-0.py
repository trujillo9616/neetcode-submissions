from heapq import heapify, heappop
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heapify(strings)
    return strings
    


def heapify_integers(integers: List[int]) -> List[int]:
    heapify(integers)
    return integers


def heap_sort(nums: List[int]) -> List[int]:
    heapify(nums)
    res = []

    while nums:
        res.append(heappop(nums))
    
    return res


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
