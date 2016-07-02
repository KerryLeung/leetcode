class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
           
        if len(nums) == 1:
            return nums[0]
            
        max_local = nums[0]
        min_local = nums[0]
        max_global = nums[0]
        i = 1
        
        while i < len(nums):
            max_local_tmp = max_local
            max_local = max( max( max_local*nums[i], nums[i] ), min_local*nums[i] )
            min_local = min( min( max_local_tmp*nums[i], nums[i] ), min_local*nums[i] )
            
            if max_local > max_global:
                max_global = max_local
            
            i += 1
            
        return max_global
