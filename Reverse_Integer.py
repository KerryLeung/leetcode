class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        sig = 1
        if x < 0:
            sig = -1
            x = -1 * x
        
        res=[]
        while x:
            i = x % 10
            x = x / 10
            res.append(i)
        
        res_num=0

        i = len(res) - 1
        while i >= 0:
            res_num += res[i] * int(math.pow(10, len(res)-i-1))
            i -= 1
            
        if res_num > math.pow(2, 31):
            return 0
        res_num = res_num * sig
        return res_num
