# Last updated: 8/18/2026, 2:50:39 PM
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C=1
        for i in range(n):
            C = C* 2*(2*i+1)/(i+2)
        return int(C)