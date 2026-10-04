class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def combination(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not visited[i]:
                    curr.append(nums[i])
                    visited[i] = True
                    combination(curr)
                    curr.pop()
                    visited[i] = False
        combination([])
        return res
            