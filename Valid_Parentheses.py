class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        if len(s) < 2:
            return False
        
        s_stack = []
        s_dict = {'(':')', '{':'}', '[':']'}
        
        for i in s:
            if i not in ['(',')', '{','}', '[',']']:
                return False
            elif i in ['(', '{', '[']:
                s_stack.append(i)
            else:
                if not s_stack or s_dict[s_stack[-1]] != i:
                    return False
                else:
                    s_stack.pop()
        
        if not s_stack:
            return True
        else:
            return False
