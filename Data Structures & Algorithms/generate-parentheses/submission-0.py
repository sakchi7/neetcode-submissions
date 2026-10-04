class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def validParenthesis(open, close, curr):
            if open == close == n:
                res.append("".join(curr))
                return
            if open < n:
                curr.append("(")
                validParenthesis(open+1, close, curr)
                curr.pop()
            if close < open:
                curr.append(")")
                validParenthesis(open, close+1, curr)
                curr.pop()

        validParenthesis(0, 0, [])
        return res