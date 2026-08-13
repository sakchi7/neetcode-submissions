class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + '#' + s
        return enc

    def decode(self, s: str) -> List[str]:
        #"5#Hello5#World"
        dec = []
        i=0
        while i<len(s):
            l = ''
            while i<len(s) and s[i] != '#':
                l += s[i]
                i+=1
            if l:
                end_index = i + 1 + int(l)
                dec.append(s[(i+1):(end_index)])
                i = end_index

        return dec
