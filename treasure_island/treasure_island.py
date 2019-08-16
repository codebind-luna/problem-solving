from typing import List

class Solution:
    def shortestPathPossible(self, x: int, y: int, map_: List[List]) -> List[int]:
        from collections import deque

        queue = deque([(x,y,None)])
        rowLength = len(map_)
        columnLength = len(map_[0])

        seen = set([(x, y)])

        def isSpotVisited(x, y):
            if (x, y) in seen:
                return True
            return False

        def isValidSpot(x, y):

            if x in range(0, rowLength) and y in range(0, columnLength):
                return True

            return False

        def isDangerousPlace(x, y):
            if map_[x][y] == 'D':
                return True

            return False

        def isGoalReached(x, y):
            if map_[x][y] == 'X':
                return True

            return False

        def GetPathFromNodes(node): 
            path = [] 
            while(node != None): 
                path.append((node[0],node[1])) 
                node = node[2] 
            return path

        while len(queue) > 0:
            parentNode = queue.popleft()
            x = parentNode[0]
            y = parentNode[1]

            if isGoalReached(x, y):
                return(GetPathFromNodes(parentNode))


            for i in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                if isValidSpot(i[0], i[1]) and \
                    (not isDangerousPlace(i[0], i[1])) \
                    and (not isSpotVisited(i[0], i[1])):
                    seen.add((i[0], i[1]))
                    queue.append((i[0], i[1], parentNode))

s = Solution()
print(s.shortestPathPossible(0,0 , [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O']
    ]))





    