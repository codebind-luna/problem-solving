from typing import List

evens = (2, 4, 6, 8)

def isEven(char: str)->int:
	if int(char) in evens:
		return 1
	else:
		return 0

def countNumberOfEvens(inputString: str)->List:
	evens = (2, 4, 6, 8)
	stringLength = len(inputString)
	countsOfEvens = [0]*stringLength
	countsOfEvens[stringLength-1] = isEven(inputString[stringLength-1])
	
	for i in range(stringLength-2, -1, -1):
		countsOfEvens[i] = countsOfEvens[i+1]
		countsOfEvens[i] += isEven(inputString[i])

	return countsOfEvens

if __name__ == '__main__':
	inputString = input("Enter the string:")
	for i in countNumberOfEvens(inputString):
		print(i, end=" ")


