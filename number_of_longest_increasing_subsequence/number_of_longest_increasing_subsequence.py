from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j in range(N):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

s = Solution()
print(s.findNumberOfLIS([1, 3, 2, 4]))

# Suppose for sequences ending at nums[i], we knew the length length[i] 
# of the longest sequence, and the number count[i] of such sequences with 
# that length.For every i < j with A[i] < A[j], we might append A[j] to a 
# longest subsequence ending at A[i]. It means that we have demonstrated 
# count[i] subsequences of length length[i] + 1.Now, if those sequences are 
# longer than length[j], then we know we have count[i] sequences of this length. 
# If these sequences are equal in length to length[j], then we know that there 
# are now count[i] additional sequences to be counted of that 
# length (ie. count[j] += count[i]).