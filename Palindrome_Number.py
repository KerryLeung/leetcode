class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        x=str(x)
        start, end = 0, len(x)-1
        while start < end:
            if x[start] != x[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
