class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1  1  2  8
        #48 24 6  1
        prefix = nums
        mulp = 1
        suffix = nums[::-1]
        muls = 1
        for i in range(len(prefix)):
            n = prefix[i]
            prefix[i] = mulp
            mulp *= n

        for i in range(len(suffix)):
            n = suffix[i]
            suffix[i] = muls
            muls *= n
        suffix.reverse()
        res = []
        for i in range(len(prefix)):
            res.append(prefix[i]*suffix[i])
        return res
