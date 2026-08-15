from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #10 22
        st = deque()
        for t in tokens:
            if t not in ('+', '-', '*', '/'):
                st.append(t)
            else:
                sec = int(st.pop())
                first = int(st.pop())
                if t == '+':
                    st.append(str(first+sec))
                elif t == '-':
                    st.append(str(first-sec))
                elif t == '*':
                    st.append(str(first*sec))
                else:
                    st.append(str(int(first/sec)))
        return int(st.pop())
        