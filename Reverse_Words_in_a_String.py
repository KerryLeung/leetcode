class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s == " "*len(s):
            return ""

        if len(s) < 2 or not isinstance(s, str):
            return s
        s=s.strip()
        array_s=[i for i in s]
        array_reverse=[array_s[len(array_s)-i-1] for i in range(len(array_s)) ]
        res_array=[]
        idx, start,end=0,0,0
        while idx < len(array_reverse):
            if array_reverse[idx]!=" ":
                start=idx
                while array_reverse[idx]!=" ":
                    idx+=1
                    if idx >= len(array_reverse):
                        break
                end=idx
                tmp_array=array_reverse[start:end]
                for i in range(len(tmp_array)):
                    res_array.append(tmp_array[len(tmp_array)-i-1])
            elif array_reverse[idx] == " ":
                while array_reverse[idx] == " ":
                    idx+=1
                res_array.append(" ")
            else:
                res_array.append(array_reverse[idx])
                idx+=1
        res_string="".join(res_array)
        res_string=res_string.strip()
        return res_string
