from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1)[::-1]:
            if nums[i] < nums[i+1]:
                idx = i+1
                for k in range(i+1, len(nums)):
                    if nums[i] < nums[k] < nums[idx]:
                        idx = k
                nums[i], nums[idx] = nums[idx], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return
        nums.sort()

        