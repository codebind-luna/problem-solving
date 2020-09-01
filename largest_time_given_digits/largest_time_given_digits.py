from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        # if 0, 1 or 2 is not present in the list then just return blank
        if 0 not in A and 1 not in A and 2 not in A:
            return ""
    
        max_time= "-9"
        # generate all the permuations of given digits
        for i in set(list(permutations(A))):    
        # keep time starting with either 0, 1, or 2. Others are invalid range.
            if 0 <= i[0] <= 2:    
                temp = str(''.join(str(t) for t in i))
         # check for 23:59 constraint
                if int(temp) <= 2359 and int(temp[2:]) < 60:    
                    if int(temp) > int(max_time):
                        max_time = temp
        
        
        if max_time == "-9":
            return ""
        else:
            return max_time[:2]+":"+max_time[2:]
