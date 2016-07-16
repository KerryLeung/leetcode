class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) < 2 or not nums:
            return []

        index_i = 0
        for i in nums:
            res_t = target - i
            if index_i == len(nums) -1:
                break
            index_j = 0
            for j in nums[index_i+1:]:
                if j == res_t:
                    return [index_i, index_i+1+index_j]
                index_j += 1
            index_i += 1
        
        return []
