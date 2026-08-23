class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        currMax = 0
        res = 0
        freq = {}
        for j in range(len(s)):
            freq[s[j]] = 1 if s[j] not in freq else freq[s[j]] + 1
            currMax = max(currMax, freq[s[j]])

            while (j-i+1)-currMax > k:
                freq[s[i]] -= 1
                i += 1
            res = max(res, j-i+1)
        return res