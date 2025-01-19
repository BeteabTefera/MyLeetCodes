class Solution(object):
    def getConcatenation(self, nums):
        '''
            U: 
        '''
        for i in range(len(nums)):
            nums.append(nums[i])
        
        return nums