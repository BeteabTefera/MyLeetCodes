class Solution:
    def countPrimes(self, num: int) -> int:
        if num <= 2 :
            return 0
        elif num == 3:
            return 1
        arry = [False for i in range(num+1)]
        limit = int(num**0.5)

        #loop through the range of n
        for i in range(2,limit+1):
            if arry[i] == False:
                # mark all the multiples of i true
                # the first index to be flipped to true is i*i
                for j in range(i*i,num+i,i):
                    if j > num:
                        break
                    arry[j] = True

        
        count = 0
        for i in arry[2:num]:
            if i == False:
                count += 1
        
        return count
