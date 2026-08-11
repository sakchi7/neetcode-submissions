class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for i in range(len(strs)):
            st = "".join(sorted(strs[i]))
            if st not in anag:
                anag[st] = [strs[i]]
            else:
                anag[st].append(strs[i])
        return list(anag.values())
        