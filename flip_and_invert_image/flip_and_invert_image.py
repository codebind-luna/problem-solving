from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[ 0 if i else 1 for i in reversed(row)] for row in A]
        