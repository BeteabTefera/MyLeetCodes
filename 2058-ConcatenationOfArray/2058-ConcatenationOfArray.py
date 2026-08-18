# Last updated: 8/18/2026, 2:49:33 PM
class Solution(object):
    def getConcatenation(self, nums):
        '''
            U: 
        '''
        for i in range(len(nums)):
            nums.append(nums[i])
        
        return nums