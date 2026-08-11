from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = defaultdict(int)
        for ch in s:
            dict_s[ch] += 1

        for ch in t:
            if (ch not in dict_s) or (dict_s[ch] == 0):
                return False
            dict_s[ch] -= 1
        return True