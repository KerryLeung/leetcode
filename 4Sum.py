class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        
        sum_val = target
        num1 = sorted(nums)
        res_list = []
        i = 0
        while i < len(num1) - 3:
            j = i + 1
            while j < len(num1) - 2:
                s = j + 1
                t = len(num1) -1
                target_val = sum_val - num1[i] - num1[j]
                while s < t:
                    t_sum = num1[s] + num1[t]
                    if t_sum > target_val:
                        t -= 1
                    elif t_sum == target_val:
                        res=[num1[i], num1[j], num1[s], num1[t]]
                        if res not in res_list:
                            res_list.append(res)
                        s += 1
                        t -= 1
                    else:
                        s += 1
                j += 1
            i += 1
  
        return res_list
