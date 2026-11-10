import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minh = nums
        self.k = k
        hq.heapify(self.minh)
        while len(self.minh) > k:
            hq.heappop(self.minh)       

    def add(self, val: int) -> int:
        hq.heappush(self.minh, val)
        if len(self.minh) > self.k:
            hq.heappop(self.minh)
        return self.minh[0]
