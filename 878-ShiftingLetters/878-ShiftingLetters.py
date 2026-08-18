# Last updated: 8/18/2026, 2:49:27 PM
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        ans = []
        shift_length = sum(shifts)
        # arr = list(s.lower())# [a,b,c]
        for i, c in enumerate(s):  #a, b, c
          # n = arr[i]
          #3+5+9, 5+9, 9
          # print(shift_length)
          # a = 97     - 97
          # z = 122    - 97
          # 0 - 25
          new_char = chr((ord(c) - 97 + shift_length) % 26 + 97)
          ans.append(new_char)
          shift_length -= shifts[i]

        return "".join(ans)
