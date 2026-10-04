class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def currSubset(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            currSubset(i+1, curr)
            while (i+1<len(nums) and nums[i]==nums[i+1]):
                i += 1
            curr.pop()
            currSubset(i+1, curr)

        currSubset(0, [])   
        return res
            
        