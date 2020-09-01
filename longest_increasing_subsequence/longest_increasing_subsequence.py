class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengthArray = len(nums)
        
        if lengthArray == 0 or lengthArray == 1:
            return lengthArray
        
        LISArray = [1] * lengthArray
        
        maxLIS = 1 

       
        for i in range(1, lengthArray):
            for j in range(i):
                if nums[i] > nums[j]:
                    LISArray[i] = max(LISArray[j] + 1, LISArray[i])
            if maxLIS < LISArray[i]:
                maxLIS = LISArray[i]
            
      
        return maxLIS
        