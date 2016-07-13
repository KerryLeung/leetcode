class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if not digits:
            return None
        
        i = len(digits) -1
        add_val = 1
        while i >= 0:
            sum = digits[i] + add_val
            if sum >= 10:
                add_val = 1
                digits[i] = sum - 10
            else:
                add_val = 0
                digits[i] = sum
            i -= 1
        
        if add_val:
            digits.insert(0, 1)
        
        return digits
