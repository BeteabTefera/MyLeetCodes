class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #ans = [(i,nums.count(i)) for i in set(nums)]
        #return max(ans, key = lambda x:x[1])[0]

        """
        - So what is the time complexity here
            - hashing set(nums) - takes O(1)
            - for i in set(nums) - worst case scenario is that there is no duplicate on original list so O(N)
            - creating tuple is O(1)
            - but nums.count(i) is O(N) worst case
                - so the operation for Space so far is creating an ans array O(N)
                    - Tuple creation for each unique I is also O(N)
                    - Space is O(N) + O(N)
                - Time Big O 
                    - O(N)
            
            now returning:
                - max -> O(N)
            
            final Time big O -> O(N) + O(N) + o(N) == O(N^2) worst case
            space O(N)
        """

        #Boyer Moore Voting algo
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate