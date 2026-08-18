# Last updated: 8/18/2026, 2:51:05 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        if len(nums) == 2: #basecase
            return [0,1]
        
        for i in range(len(nums)): # i = 0 ,
            for j in range(i + 1, len(nums)): # j = 1
                if nums[i] + nums [j] == target: 
                    return [i,j]
                    break
            
