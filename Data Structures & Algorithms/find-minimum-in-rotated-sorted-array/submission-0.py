class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = 9999
        l = 0
        r = len(nums) - 1
        while l<=r:
            m = l + (r - l)//2
            minNum = min(minNum, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return minNum
        