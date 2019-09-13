from typing import List 

def count(denominationsArray: List,numberOfTypes: int, target: int)->int:
	solutionTable = [[0 for _ in range(numberOfTypes)] 
								for _ in range(target+1)]

	for i in range(numberOfTypes): 
		solutionTable[0][i] = 1

	# Fill rest of the solutionTable entries in bottom up manner 
	for i in range(1, target+1): 
		for j in range(numberOfTypes): 

			# Count of solutions including denominationsArray[j] 
			x = solutionTable[i - denominationsArray[j]][j] if i-denominationsArray[j] >= 0 else 0

			# Count of solutions excluding denominationsArray[j] 
			y = solutionTable[i][j-1] if j >= 1 else 0

			# total count 
			solutionTable[i][j] = x + y 

	return solutionTable[target][numberOfTypes-1] 

if __name__ == '__main__':
	numberOfTypes = int(input())

	denominationsArray = list(map(int, input().split()))
	denominationsArray.sort()


	for i in range(denominationsArray[-1], denominationsArray[-1]*2 + 1):
		if not count(denominationsArray, numberOfTypes, i):
			print(i)
			break

	print('Fake Offer!')
