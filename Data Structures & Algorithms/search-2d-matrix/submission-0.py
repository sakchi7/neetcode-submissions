class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        cols = len(matrix[0])
        while (l<=r):
            mid = l + (r-l)//2
            if (target >= matrix[mid][0] and target <= matrix[mid][cols-1]):
                break
            elif (target<matrix[mid][0]):
                r = mid - 1
            else:
                l = mid + 1
        l = 0
        r = cols-1
        while (l<=r):
            m = l + (r-l)//2
            if (target == matrix[mid][m]):
                return True
            elif target > matrix[mid][m]:
                l = m+1
            else:
                r = m-1
        return False
        