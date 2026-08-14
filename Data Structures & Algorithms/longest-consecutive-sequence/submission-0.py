class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return len(nums)
        i = 0
        j = 1
        maxlen = -1
        curr = 1
        while j<len(nums):
            if nums[j]-nums[i]==1:
                curr += 1
            elif nums[j]-nums[i]==0:
                curr = curr
            else:
                maxlen = max(maxlen, curr)
                curr = 1                
            i = j
            j += 1
        maxlen = max(maxlen, curr)
        return maxlen
        