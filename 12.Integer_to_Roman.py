# 40ms, faster than 95.24%
# 12.8MB, less than 100%
class Solution:
    def intToRoman(self, num: int) -> str:
        intList = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        strList = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        out = ''
        i = 0
        while num > 0:
            out += strList[i] * (num // intList[i])
            num %= intList[i]
            i += 1
        return out
