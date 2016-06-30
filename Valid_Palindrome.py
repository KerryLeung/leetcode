class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 1 or s == " "*len(s):
            return True
        
        i, j = 0, len(s)-1
        while i < j:
            while not ( (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= '0' and s[i] <= '9') ) and i < len(s)-1:
                i += 1
            
            while not ( (s[j] >= 'a' and s[j] <= 'z') or (s[j] >= 'A' and s[j] <= 'Z') or (s[j] >= '0' and s[j] <= '9') ) and j > 0:
                j -= 1
            
            if i >= j:
                return True
                       
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
            
        return True
