class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []
        def subset(index):
            if index >= len(nums):
                ans.append(res.copy())
                return
            res.append(nums[index])
            subset(index+1)
            res.pop()
            subset(index+1)
        subset(0)
        return ans
        