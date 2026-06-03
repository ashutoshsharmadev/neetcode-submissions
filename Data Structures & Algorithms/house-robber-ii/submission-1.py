class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # nums[0] in case we only have one element
        # skipping first house and then another for skipping last house
        return max(nums[0], self.helper(nums[1:]) ,self.helper(nums[:-1]))
    
    
    def helper(self, nums):
        rob1, rob2 = 0,0
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2