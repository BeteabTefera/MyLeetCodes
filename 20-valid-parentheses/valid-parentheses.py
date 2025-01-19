class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #create a relationship 
        rel = {'(':')', '{':'}', '[':']'}
        #base case
        if len(s) <= 1 or s[0] in  (')', '}', ']') :
            return False
        
        #stack implementation
        stack = []

        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                try:
                    if rel[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
                except:
                    return False
    
        return True if not stack else False
        