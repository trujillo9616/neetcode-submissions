class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dis_to_origin(p: List[int]) -> float:
            return math.sqrt((p[0])**2 + (p[1])**2)
        
        heap = []

        for point in points:
            heapq.heappush(heap, (-dis_to_origin(point), point))

            if len(heap) > k:
                heapq.heappop(heap)
        

        return [point for dis, point in heap]