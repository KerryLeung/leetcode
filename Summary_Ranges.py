class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
            
        if len(nums) == 1:
            return ["->".join(map(lambda x: str(x), nums))]
        
        res=[]
        i=0
        while i<len(nums):
            k=i
            j=i+1
            while(j < len(nums)):
                if nums[j] == nums[i]+1:
                    i+=1
                    j+=1
                else:
                    break
            if k==i:
                res.append("->".join(map(lambda x: str(x), [nums[k]])))
            else:
                res.append("->".join(map(lambda x: str(x), [nums[k], nums[i]])))
            i+=1
            
        return res    
            
        
