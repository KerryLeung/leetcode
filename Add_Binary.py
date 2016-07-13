class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
            
        if not b:
            return a
        
        la = len(a)
        lb = len(b)
        
        if la > lb:
            b = "0" * (la - lb) + b
        else:
            a = "0" * (lb - la) + a

        add_val = 0
        i = len(a) - 1
        res=['0']*len(a)
        while i >= 0 :
            new_val = 0
            if a[i] == '1' and b[i] == "1":
                res[i] = str(add_val)
                add_val = 1
            elif a[i] == '1' or b[i] == '1':
                if add_val:
                    res[i] = '0'
                    add_val = 1
                else:
                    res[i] = '1'
                    add_val = 0                    
            else:
                res[i] = str(add_val)
                add_val = 0
            i -= 1
        res_str = "".join(res)
        if add_val: res_str = "1" + res_str
        return res_str
