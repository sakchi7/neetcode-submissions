from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for n in nums:
            num_dict[n] += 1

        sorted_dict = dict(sorted(num_dict.items(), key=lambda item:item[1], reverse=True))
        res = []
        for x in list(sorted_dict.keys()):
            if k>0:
                res.append(x)
                k-=1
        return res