class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
            
        def bin_search(array, start, end, n):
            while start <= end:
                mid = (end + start) / 2
                if array[mid] > n:
                    end = mid - 1
                elif array[mid] == n:
                    return True
                else:
                    start = mid + 1
            return False
            
        start, end = 0, len(matrix)
        start_index, end_index = 0, len(matrix[0]) - 1
        while start < end:
            if start_index == end_index:
                if matrix[start][start_index] == target:
                    return True
                else:
                    start += 1
            else:
                if matrix[start][start_index] <= target and matrix[start][end_index] >= target:
                    break
                else:
                    start += 1
                
        if start == end:
            return False
        else:
            return bin_search(matrix[start], start_index, end_index, target)
