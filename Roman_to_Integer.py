class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res, i= 0, len(s) -1
        while i >=0:
            if i == len(s) - 1:
                res = romanDict[s[i]]
            else:
                if romanDict[s[i]] >= romanDict[s[i+1]]:
                    res += romanDict[s[i]]
                else:
                    res -= romanDict[s[i]]
            i -= 1
        return res
