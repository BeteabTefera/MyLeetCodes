# Last updated: 8/18/2026, 2:50:20 PM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #log time based solution
        res = ""
        while columnNumber > 0:
            offSet = (columnNumber-1) % 26
            res += chr(ord('A') + offSet)
            columnNumber = (columnNumber - 1)//26

        return res [::-1]