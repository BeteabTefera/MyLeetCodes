# Last updated: 8/18/2026, 2:49:44 PM
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num += 2**32

        hex_car = "0123456789abcdef"
        res = ""

        while num > 0:
            res = hex_car[num%16] + res
            num //= 16

        return res