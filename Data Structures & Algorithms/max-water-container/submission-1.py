class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(heights) - 1
        while (i<j):
            currArea = (j-i) * min(heights[i], heights[j])
            maxArea = max(maxArea, currArea)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return maxArea
        