class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = set()
        
        for i, v in enumerate(nums):
            complementaryNumber = target-v
            if complementaryNumber in numbers:
                return [nums.index(complementaryNumber), i]
            else:
                numbers.add(v)