class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        sum_val = 0
        num1 = sorted(nums)
        res_list = []
        i = 0
        while i < len(num1) - 2:
            s = i + 1
            t = len(num1) -1
            target_val = sum_val - num1[i]
            while s < t:
                t_sum = num1[s] + num1[t]
                if t_sum > target_val:
                    t -= 1
                elif t_sum == target_val:
                    res=[num1[i], num1[s], num1[t]]
                    if res not in res_list:
                        res_list.append(res)
                    s += 1
                    t -= 1
                else:
                    s += 1
            i += 1
  
        return res_list
                
            
