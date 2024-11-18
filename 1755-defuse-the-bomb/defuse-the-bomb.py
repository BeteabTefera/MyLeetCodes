class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        #base case
        if k == 0:
            code = [0] * len(code)
            return code

        #initializing the result array
        result = [0] * n

        for i in range(n):
            total = 0

            if k > 0:
                for j in range(1,k+1):
                    total += code[(i+j) % n]

            elif k < 0:
                for j in range(1,abs(k) + 1):
                    total += code [(i-j)% n]
            result[i] = total
        return result