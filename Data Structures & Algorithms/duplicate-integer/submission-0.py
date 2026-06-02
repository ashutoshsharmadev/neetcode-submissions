class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = []
        for i in nums:
            if i in x:
                return(True)
            x.append(i)
        return False