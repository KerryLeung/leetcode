class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_list=["a","e","i","o","u", "A", "E", "I", "O", "U"]
        if len(s) < 2:
            return s
        
        array_s=[i for i in s]
        
        start=0
        end=len(s)-1
        while start < end:
            while start < len(s) and array_s[start] not in vowels_list:
                start+=1
            while end > 0 and array_s[end] not in vowels_list:
                end-=1
            if start < end:
                t=array_s[start]
                array_s[start]=array_s[end]
                array_s[end]=t
                start+=1
                end-=1
                
        return ("").join(array_s)
        
        
