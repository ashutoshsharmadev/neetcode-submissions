class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, path):
            # add a copy of the solution to final if pass
            if index == len(nums):
                result.append(path[:])
                return
            # constraint check
            # fail -> continue
            
            #pass -> add element / make choice
            # backtrack using new choice
            # undo choice

            #decision 1 : include nums[index]
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            #decision 2 : dont include nums[index]
            backtrack(index + 1, path)

        backtrack(0,[])
        return result