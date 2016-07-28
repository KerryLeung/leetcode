class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                res.append(nums2[j])
                j += 1
                continue
            
            if j == len(nums2):
                res.append(nums1[i])
                i += 1
                continue
            
            if nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.append(nums1[i])
                i += 1
            
        total_num = len(nums1) + len(nums2)
        if total_num % 2 == 0:
            return float(res[total_num/2-1] + res[total_num/2])/float(2)
        else:
            return float(res[total_num/2])
            
