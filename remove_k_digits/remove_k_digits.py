class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        # we need to remove the peak element from the left k times
        
        for number in num:
            while len(stack)>0 and stack[-1]>number and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(number)
        
        #if we need to remove more digits
        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        #check for leading 0
        i = 0
        n = len(stack)
        while i < n and stack[i]=='0':
            i += 1
        if len(stack[i:])>0:
            return ''.join(stack[i:])
        else:
            return '0'