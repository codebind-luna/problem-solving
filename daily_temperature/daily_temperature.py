class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        res = [0]*length
        stack = []
        for i in range(length):
            # If current number is bigger, we solved the previous puzzles
            while len(stack) != 0 and T[i] > T[stack[-1]]:
                k = stack.pop()
                # t[i] is the next bigger number than t[k]
                res[k] = i-k
            stack.append(i)
        return res
