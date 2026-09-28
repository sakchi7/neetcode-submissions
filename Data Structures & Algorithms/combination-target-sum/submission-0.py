class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def currSum(i, curr, sum):
            if sum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or sum > target:
                return

            curr.append(nums[i])
            currSum(i, curr, sum+nums[i])
            curr.pop()
            currSum(i+1, curr, sum)

        currSum(0, [], 0)
        return res
        