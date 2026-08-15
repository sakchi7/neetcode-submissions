from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for ch in s:
            if ch in ('(', '{', '['):
                st.append(ch)
            else:
                top = st.pop() if len(st)>0 else ''
                if (ch==']' and top!='[') or (ch=='}' and top!='{') or (ch==')' and top!='('):
                    return False
        return True if len(st)==0 else False