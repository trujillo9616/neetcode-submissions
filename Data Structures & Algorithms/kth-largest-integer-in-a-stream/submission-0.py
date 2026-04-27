from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)

        while len(nums) > k:
            heappop(nums)
        
        self.heap = nums
        self.k = k

    
    def add(self, val: int) -> int:
        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)
        
        return self.heap[0]
