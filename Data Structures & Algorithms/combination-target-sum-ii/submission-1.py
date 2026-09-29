class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def currComb(i, curr, sumc):
            if sumc == target:
                res.append(curr.copy())
                return
            if sumc > target or i >= len(candidates):
                return
            if sumc + candidates[i] > target:
                return
            curr.append(candidates[i])
            currComb(i+1, curr, sumc+candidates[i])
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            currComb(i+1, curr, sumc)

        currComb(0, [], 0)
        return res
