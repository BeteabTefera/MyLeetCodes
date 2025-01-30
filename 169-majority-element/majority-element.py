class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [(i,nums.count(i)) for i in set(nums)]
        return max(ans, key = lambda x:x[1])[0]