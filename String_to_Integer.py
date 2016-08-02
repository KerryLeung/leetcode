class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str or str[0] not in ('-', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            return 0

        if len(str) == 1 and str[0] not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            return 0
            
        sig = 1
        if str[0] == '-':
            sig = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
            
        index = 0
        for s in str:
            if s not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                if index == 0:
                    return 0
                else:
                    str=str[0:index]
                    break
            index += 1
        
        i = 0
        while i < len(str):
            if str[i] == '0':
                i += 1
            else:
                break
            
        if i == len(str):
            return 0
        else:
            str = str[i:]
        
        import math
        max_num = math.pow(2, 31)
        if len(str) > 10:
            if sig == 1:
                return 2147483647
            else:
                return -2147483648

        if int(str) > max_num:
            if sig == 1:
                return 2147483647
            else:
                return -2147483648
        elif int(str) == max_num and sig == 1:
            return sig * (int(str) - 1)
        else:
            return sig * int(str)
        
            
        
        
