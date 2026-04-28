class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        min_heap = []
        for num in count.keys():
            heapq.heappush(min_heap, (count[num], num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for _count, num in min_heap]