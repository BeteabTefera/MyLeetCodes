class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0 or s[0] in (']','}',')'): # Base Case: this will check if the first element is an outie, that is an instant False
            return False
        #first and foremost get a dict variable to hold the closing bracket and its corresponding innie
        dict1 = {']':'[',')':'(','}':'{'}
        #initialize the stack variable that will hold the char
        stack = []

        #loop through the string 
        #second submission to optimize the code
        for i in s: 
            if i in ('[','{','('): #thi checkes if i is one of the openers to append
                stack.append(i) 
            else:
                try:
                    if stack.pop() == dict1[i]: #this will just use the fact that pop returns value to pop out the top and also validate at the same time
                        continue
                    else:
                        return False
                except:
                    return False
        return len(stack) == 0 #ultimately this can only be reached if the stack is empty