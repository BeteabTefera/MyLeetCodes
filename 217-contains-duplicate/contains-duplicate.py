class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #dicts = {i:nums.count(i) for i in nums}
        
        return False if len(nums) == len(set(nums)) else True