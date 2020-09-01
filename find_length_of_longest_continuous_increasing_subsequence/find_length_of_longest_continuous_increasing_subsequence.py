from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        total_numbers = len(nums)
        
        if total_numbers <= 1:
            return total_numbers
        
        length_of_LICS = 0
        dp = [1] * total_numbers
        for i in range(1, total_numbers):
            
            if nums[i] > nums[i-1]:
                dp[i] = dp[i - 1] + 1
                
            if length_of_LICS < dp[i]:
                length_of_LICS = dp[i]
                
        return length_of_LICS
