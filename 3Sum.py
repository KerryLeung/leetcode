class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        def bin_search(array, start, end, target):
            while start <= end:
                mid = (start + end) / 2
                if array[mid] > target:
                    end = mid -1 
                elif array[mid] == target:
                    return mid
                else:
                    start = mid + 1
            return -1
        
        sum_val = 0
        num1 = sorted(nums)
        res_list = []
        i = 0
        while i < len(num1) - 2:
            j = i + 1
            while j < len(num1) - 1:
                target_val = sum_val - num1[i] - num1[j]
                pos = bin_search(num1, j+1, len(num1)-1, target_val)
                if pos != -1:
                    res=[num1[i], num1[j], num1[pos]]
                    if sorted(res) not in res_list:
                        res_list.append(sorted(res))
                j += 1
            i += 1
        
        return res_list
                
            
