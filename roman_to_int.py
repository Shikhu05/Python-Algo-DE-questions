class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            'I':1, 'V':5, 'X':10, 'L':50, 
            'C':100, 'D':500, 'M':1000
        }

        num = 0 
        p = 0
        for i in reversed(s):
            value = int(dct[i])

            if value < p: 
                num -= value 
                p = p - value 
            else:
                num += value 
                p = value 
        return num



