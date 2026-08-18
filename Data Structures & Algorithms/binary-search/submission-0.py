class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = 0
        n = len(nums)-1
        while (m<=n):
            mid = m + (n-m)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                n = mid - 1
            else:
                m = mid + 1
        return -1
        