#mmmm ~ group theor ~ yeeeeeeee

import string
import numpy as np

class LatinSquare:
	#size refers to the size of the group that the latin square is created for, not the size of the array

	def __init__(self, size, square):
		self.size = size
		self.square = square

	def displaySquare(self):
		print("-----------------------")
		for i in range(0, self.size**2, self.size):
			for j in range(self.size):
				print(self.square[(i//self.size*self.size)+j] , " ", end="")
			print()
		print("-----------------------")

	def changeElement(self, row, col, element):
		self.square[(row*self.size)+col] = element
	
	def isValid(self, groupSet):
		firstRow = []
		firstCol = []
		for j in range(self.size):
			firstRow.append(self.square[j])
		for j in range(self.size):
			firstCol.append(self.square[(j*self.size)])
		if "".join(str(x) for x in firstRow) != "".join(str(x) for x in firstCol):
			return False
		rowTest = set()
		for i in range(0, self.size**2, self.size):
			test = set()
			for j in range(self.size):
				test.add(self.square[(i//self.size*self.size)+j])
			test.intersection_update(groupSet)
			if len(test)<self.size:
				return False
		for i in range(self.size):
			test = set()
			for j in range(self.size):
				test.add(self.square[(j*self.size)+i])
			test.intersection_update(groupSet)
			if len(test)<self.size:
				return False
		return True

	def isIsomorphicTo(self, otherGroupSquare):
		if self.size != otherGroupSquare.size:
			return False

		tempTable1 = self.square[:]
		tempTable2 = otherGroupSquare.square[:]

		string1 = "".join(str(x) for x in tempTable1)
		string2 = "".join(str(x) for x in tempTable2)
		for i in range(self.size):
			string1 = string1.replace(string1[i], str(i))
			string2 = string2.replace(string2[i], str(i))

		return string1==string2

	def isFull(self):
		for i in range(self.size**2):
			if self.square[i]=="-":
				return False
		return True

	def isSymmetric(self):
		for i in range(0, self.size**2, self.size):
			for j in range(self.size):
				if self.square[(i//self.size*self.size)+j] != self.square[( j*self.size)+(i//self.size)]:
					return False
		# self.displaySquare()
		return True

	def isCyclic(self):
		count = 0
		for i in range(self.size):
			if self.square[i*self.size + i]==0:
				count+=1
		if count!=2:
			return False
		return True
	
	def isAssociative(self):
		array = self.square[:]
		stringOfArray = "".join(str(x) for x in array)
		for i in range(self.size):
			stringOfArray = stringOfArray.replace(stringOfArray[i], str(i))

		for i in range(self.size):
			for j in range(self.size):
				for k in range(self.size):
					# (ab)c = a(bc)
					# a = i
					# b = j
					# c = k
					ab = int(stringOfArray[i*self.size + j])
					# c = k
					abc1 = int(stringOfArray[ab*self.size + k])

					# a = i
					bc = int(stringOfArray[j*self.size + k])
					abc2 = int(stringOfArray[i*self.size + bc])

					if abc1 != abc2:
						# print(i, j, k)
						return False
		return True

	def optionsForThisPosition(self, row, col, groupSet):
		possibilities = set(list(groupSet)[:])
		usedSymbols = set()
		for j in range(self.size):
			usedSymbols.add( self.square[(row*self.size)+j])
		for j in range(self.size):
			usedSymbols.add( self.square[(j*self.size)+col] )
		possibilities.difference_update(usedSymbols)
		return list(possibilities)



def bruteForce(square, groupSet):

	if square.isFull():
		if (square.isValid(groupSet)!=True):
			return ""
		if square.isAssociative():
			return ""
		return square
	else:
		for i in range(square.size**2):
			if square.square[i]=="-":
				for symbol in square.optionsForThisPosition(i//square.size, i%square.size, groupSet):
					temp = square.square[:]
					temp[i] = symbol
					newSquare = LatinSquare(square.size, temp[:])
					result = bruteForce(newSquare, groupSet)
					if result!="":
						if result.isValid(groupSet):
							# result.displaySquare()
							return result
				break
	return ""

def bruteForce11(square, groupSet):
	if square.isFull():
		if (square.isValid(groupSet)!=True):
			return ""
		# square.displaySquare()
		if square.isAssociative():
			return ""
		if square.isSymmetric():
			# result.displaySquare()
			return square
		return ""
	else:
		for i in range(square.size**2):
			if square.square[i]=="-":
				for symbol in square.optionsForThisPosition(i//square.size, i%square.size, groupSet):
					temp = square.square[:]
					temp[i] = symbol
					newSquare = LatinSquare(square.size, temp[:])
					result = bruteForce11(newSquare, groupSet)
					if result!="":
						if result.isValid(groupSet):
							# result.displaySquare()
							return result
				break
	return ""

def bruteForce12(square, groupSet):
	if square.isFull():
		if (square.isValid(groupSet)!=True):
			return ""
		if square.isAssociative() != True:
			return ""
		if square.isSymmetric() != True:
			return square
		return ""
	else:
		for i in range(square.size**2):
			if square.square[i]=="-":
				for symbol in square.optionsForThisPosition(i//square.size, i%square.size, groupSet):
					temp = square.square[:]
					temp[i] = symbol
					newSquare = LatinSquare(square.size, temp[:])
					result = bruteForce12(newSquare, groupSet)
					if result!="":
						if result.isValid(groupSet):
							return result
				break
	return ""

def bruteForce13(square, groupSet):
	if square.isFull():
		if (square.isValid(groupSet)!=True):
			return ""
		if square.isAssociative() != True:
			return ""
		if square.isSymmetric() == True:
			return ""
		if square.isCyclic() != True:
			return square
		return ""
	else:
		for i in range(square.size**2):
			if square.square[i]=="-":
				for symbol in square.optionsForThisPosition(i//square.size, i%square.size, groupSet):
					temp = square.square[:]
					temp[i] = symbol
					newSquare = LatinSquare(square.size, temp[:])
					result = bruteForce13(newSquare, groupSet)
					if result!="":
						if result.isValid(groupSet):
							return result
				break
	return ""


def main():
	symbols = list(string.ascii_lowercase)

	size = 8
	# create initial element table
	array = ["-"] * (size**2)
	groupSet = set( [ x for x in range(size) ] )
	square = LatinSquare(size, array)
	for i in range(size):
		square.changeElement(0, i, i)
		square.changeElement(i, 0, i)
	square.displaySquare()


	#instantiate
	#------------------------------------------------------------------------------------------------------------------------------------------
	# 6 element group
	# groupSet = set([0,1,2,3,4,5])

	# 5 element group
	# groupSet = set([0,1,2,3,4])

	# 4 element group
	# groupSet = set([0,1,2,3])

	# 5 element initial square
	# array = [0,1,2,3,4,1,"-","-","-","-",2,"-","-","-","-",3,"-","-","-","-",4,"-","-","-","-"]

	# 6 element initial square
	# array = [0,1,2,3,4,5,1,"-","-","-","-","-",2,"-","-","-","-","-",3,"-","-","-","-","-",4,"-","-","-","-","-",5,"-","-","-","-","-"]

	# 4 element initial square
	# array = [0,1,2,3,1,"-","-","-",2,"-","-","-",3,"-","-","-"]

	#------------------------------------------------------------------------------------------------------------------------------------------

	# 
	# 5 element initial square
	# array = [0,1,2,3,4,1,"-","-","-","-",2,"-","-","-","-",3,"-","-","-","-",4,"-","-","-","-"]
	# groupSet = set([0,1,2,3,4])
	# square = LatinSquare(5, array)
	# newSquare = bruteForce(square, groupSet)

	# 
	# 6 element initial square
	# array = [0,1,2,3,4,5,1,"-","-","-","-","-",2,"-","-","-","-","-",3,"-","-","-","-","-",4,"-","-","-","-","-",5,"-","-","-","-","-"]
	# groupSet = set([0,1,2,3,4,5])
	# square = LatinSquare(6, array)
	# newSquare = bruteForce11(square, groupSet)



	# 
	# 6 element initial square
	# array = [0,1,2,3,4,5,1,"-","-","-","-","-",2,"-","-","-","-","-",3,"-","-","-","-","-",4,"-","-","-","-","-",5,"-","-","-","-","-"]
	# groupSet = set([0,1,2,3,4,5])
	# square = LatinSquare(6, array)
	# newSquare = bruteForce12(square, groupSet)

	#
	# 8 element initial square
	# array = [0,1,2,3,4,5,6,7,1,0,"-","-","-","-","-","-",2,"-","-","-","-","-","-","-",3,"-","-","-","-","-","-","-",4,"-","-","-","-","-","-","-",5,"-","-","-","-","-","-","-",6,"-","-","-","-","-","-","-",7,"-","-","-","-","-","-","-"]
	# groupSet = set([0,1,2,3,4,5,6,7])
	# square = LatinSquare(8, array)
	newSquare = bruteForce13(square, groupSet)
	# print(square.isCyclic())

	newSquare.displaySquare()

	# print(newSquare.isAssociative())

if __name__ == "__main__": 
	main()