import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minSpeed = r
        while (l<=r):
            mid = (l + r)//2
            time = 0
            for p in piles:
                time += math.ceil(float(p)/mid)
            if time <= h:
                minSpeed = mid
                r = mid - 1
            else:
                l = mid + 1
        return minSpeed

        