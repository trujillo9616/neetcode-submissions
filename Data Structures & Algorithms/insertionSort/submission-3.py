# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        state = []

        def log_state():
            state.append(pairs.copy())
        
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        log_state()
        for i in range(1, len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j+1].key < pairs[j].key:
                swap(pairs, j+1, j)
                j -= 1
            
            log_state()

        return state