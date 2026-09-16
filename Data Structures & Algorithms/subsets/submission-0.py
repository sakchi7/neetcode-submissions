class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def subset(i:int):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            subset(i+1)
            sub.pop()
            subset(i+1)
        subset(0)
        return res
        