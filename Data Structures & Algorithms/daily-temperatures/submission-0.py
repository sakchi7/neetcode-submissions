from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = deque()
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while i < len(temperatures) and len(temp)>0 and temperatures[i]>temperatures[temp[-1]]:
                val = temp.pop()       
                res[val] = i-val
            temp.append(i)
        return res
        
        