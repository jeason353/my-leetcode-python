# 52ms, faster than 55.06%
# 12.7MB, less than 100%
class Solution:
    def romanToInt(self, s: str) -> int:
        intList = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        strList = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        out = 0
        i = 0
        while len(s) > 0:
            while s[0:len(strList[i])] == strList[i]:
                out += intList[i]
                s = s[len(strList[i]):]
                if len(s) == 0:
                    break
            i += 1
        return out