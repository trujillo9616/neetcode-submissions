class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = [0 ,0]

        for num in nums:
            temp = max(num + rob[0], rob[1])
            rob[0] = rob[1]
            rob[1] = temp
        
        return rob[1]
