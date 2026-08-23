class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxStr = 0
        subStr = set()
        for j in range(len(s)):
            while (i<j and s[j] in subStr):
                subStr.remove(s[i])
                i += 1
            subStr.add(s[j])
            maxStr = max(maxStr, (j-i+1))
        return maxStr
        