class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def convert(num):
            a=[]
            i=num
            while i != 0:
                j=i%10
                i=i/10
                a.append(j)
            res=0
            for i in a:
                res+=i
            return res
        
        if not isinstance(num, int) or num < 0:
            return num
            
        sum=convert(num)
        while sum >= 10:
            sum=convert(sum)
            
        return sum
        
                
