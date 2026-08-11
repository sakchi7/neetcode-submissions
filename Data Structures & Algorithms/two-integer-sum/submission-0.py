class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        res = []
        for i in range(len(nums)):
            if (target - nums[i]) in dict_num:
                res = [i, dict_num[target - nums[i]]]
                break
            else:
                dict_num[nums[i]] = i
        return sorted(res)