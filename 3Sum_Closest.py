class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) < 3:
            return []
        
        sum_val = target
        num1 = sorted(nums)
        closest_num = 0
        closest_diff = 0
        i = 0
        while i < len(num1) - 2:
            s = i + 1
            t = len(num1) -1
            target_val = sum_val - num1[i]
            while s < t:
                t_sum = num1[s] + num1[t]
                if t_sum > target_val:
                    t -= 1
                    if closest_diff == 0 or t_sum - target_val < abs(closest_diff):
                        closest_diff = t_sum - target_val
                        closest_num = t_sum+ num1[i]
                elif t_sum == target_val:
                    return sum_val
                else:
                    s += 1
                    if closest_diff == 0 or target_val - t_sum < abs(closest_diff):
                        closest_diff = t_sum - target_val
                        closest_num = t_sum+ num1[i]
            i += 1
  
        return closest_num
