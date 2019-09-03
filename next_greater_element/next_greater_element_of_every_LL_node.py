from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        resultArray, stack = [], []
        i = 0
        while head:
            resultArray.append(0)
            val = head.val
            while stack and stack[-1][1] < val:
                res[stack.pop()[0]] = val
            stack.append((i, val))
            head = head.next
            i += 1

        return res
