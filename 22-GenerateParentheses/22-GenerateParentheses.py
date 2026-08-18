# Last updated: 8/18/2026, 2:50:52 PM
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        Understand: Finding if a parentheses is valid. 

        
        """
        res = []
        def backtrack(s, open=0, close=0):
            if len(s) == n*2:
                res.append(s)
            if open < n:
                backtrack(s + "(", open+1, close)
            if close < open:
                backtrack(s + ")", open, close+1)

        backtrack('',0,0)
        return res
            