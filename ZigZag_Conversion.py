class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or len(s) <= 1 or numRows <= 1:
            return s
        
        res_arr = []
        i = 0
        while i < numRows: 
            res_arr.append([])
            i += 1
        index = 0
        for v in s:
            row_num = index % (2*numRows -2)
            if row_num < numRows:
                res_arr[row_num].append(v)
            else:
                res_arr[2*numRows - 2 - index%(2*numRows -2)].append(v)
            index += 1
        
        res = ""
        for s1 in res_arr:
            for s2 in s1:
                res += s2
        return res
