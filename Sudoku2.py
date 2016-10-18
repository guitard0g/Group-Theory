#---------------#
#Joshua Learn	#
# Period 1		#
# 11/17/14		#
#---------------#

from copy import deepcopy
from time import clock
START_TIME = clock()

h = 9

def main():
	matrix = create()
	display(matrix)
	matrix = recurToSolve(matrix)
	display(matrix)

class cell(object):
	matrix = None
	def __init__(self, val, r, c, matrix):
		if val!= 0:
			self.value = {val,}
		else:
			self.value = {1,2,3,4,5,6,7,8,9,}
		self.row = r
		self.col = c
		self.block = blockNumber(self, r, c)
		cell.matrix = matrix

def display(matrix):
	for row in range(h):
		for col in range(h):
			v = matrix[row][col].value
			if len(v) != 1:
				print('-', end='  ')
			else:
				print(list(v)[0], end='  ')
		print()
	print()

def create():
	M1 = [[4,8,1,5,0,9,6,7,0],
		[3,0,0,8,1,6,0,0,2],
		[5,0,0,7,0,3,0,0,8],
		[2,0,0,0,0,0,0,0,9],
		[9,0,0,0,0,0,0,0,1],
		[8,0,0,0,0,0,0,0,4],
		[0,3,9,2,7,5,4,8,0],
		[6,0,0,0,0,0,9,2,7],
		[7,0,0,0,0,0,3,1,0],]
	M2 = 	[[6,0,0,0,4,8,0,0,2],
			[8,0,0,5,2,0,0,4,0],
			[0,0,0,0,0,7,0,0,0],
			[5,0,0,4,0,3,0,2,0],
			[0,0,1,0,0,0,9,0,0],
			[0,2,0,9,0,5,0,0,8],
			[0,0,0,7,0,0,0,0,0],
			[0,1,0,0,9,2,0,0,5],
			[2,0,0,8,6,0,0,0,3]]
	M3 = 	[[8,0,0,0,0,0,0,0,0],
			[0,0,3,6,0,0,0,0,0],
			[0,7,0,0,9,0,2,0,0],
			[0,5,0,0,0,7,0,0,0],
			[0,0,0,0,4,5,7,0,0],
			[0,0,0,1,0,0,0,3,0],
			[0,0,1,0,0,0,0,6,8],
			[0,0,8,5,0,0,0,1,0],
			[0,9,0,0,0,0,4,0,0]]

	matrix = []
	for r in range(h):
		row = []
		for c in range(h):
			row.append(cell(M3[r][c], r, c, matrix))
		matrix.append(row)

	return matrix

def restoreMatrix(matrix, oldMatrix):
	for r in range(h):
		for c in range(h):
			matrix[r][c].value = oldMatrix[r][c].value
	return matrix

def recurToSolve(matrix):
	matrix = fillInEasies(matrix)
	if badMatrix(matrix) or isCorrect(matrix):
		return matrix
	oldMatrix = deepcopy(matrix)
	r, c = coordinatesOfCellWithMinOptions(matrix)
	for guess in matrix[r][c].value:
		matrix[r][c].value = {guess,}
		matrix = recurToSolve(matrix)
		if isCorrect(matrix):
			return matrix
		matrix = restoreMatrix(matrix, oldMatrix)
	return matrix

def blockNumber(self, row, col):
	if (self.row < 3) and (self.col < 3): return 0
	if (self.row < 3) and (2 < self.col < 6): return 1
	if (self.row < 3) and (5 < self.col): return 2
	if (2 < self.row < 6) and (self.col < 3): return 3
	if (2 < self.row < 6) and (2 < self.col < 6): return 4
	if (2 < self.row < 6) and (5 < self.col): return 5
	if (5 < self.row ) and (self.col < 3): return 6
	if (5 < self.row) and (2 < self.col < 6): return 7
	if (5 < self.row) and (5 < self.col): return 8


def badMatrix(matrix):
	for r in range(h):
		for c in range(h):
			if matrix[r][c].value == set():
				return True
	return False

def isCorrect(matrix):
	rows = [[],[],[],[],[],[],[],[],[],]
	cols = [[],[],[],[],[],[],[],[],[],]
	for r in range(h):
		for c in range(h):
			rows[r].append(matrix[r][c].value)
			cols[c].append(matrix[r][c].value)

	block = [[],[],[],[],[],[],[],[],[],]

	block[0] = [matrix[0][0].value, matrix[0][1].value, matrix[0][2].value,
				matrix[1][0].value, matrix[1][1].value, matrix[1][2].value,
				matrix[2][0].value, matrix[2][1].value, matrix[2][2].value,]
	block[1] = [matrix[0][3].value, matrix[0][4].value, matrix[0][5].value,
				matrix[1][3].value, matrix[1][4].value, matrix[1][5].value,
				matrix[2][3].value, matrix[2][4].value, matrix[2][5].value,]
	block[2] = [matrix[0][6].value, matrix[0][7].value, matrix[0][8].value,
				matrix[1][6].value, matrix[1][7].value, matrix[1][8].value,
				matrix[2][6].value, matrix[2][7].value, matrix[2][8].value,]
	block[3] = [matrix[3][0].value, matrix[3][1].value, matrix[3][2].value,
				matrix[4][0].value, matrix[4][1].value, matrix[4][2].value,
				matrix[5][0].value, matrix[5][1].value, matrix[5][2].value,]
	block[4] = [matrix[3][3].value, matrix[3][4].value, matrix[3][5].value,
				matrix[4][3].value, matrix[4][4].value, matrix[4][5].value,
				matrix[5][3].value, matrix[5][4].value, matrix[5][5].value,]
	block[5] = [matrix[3][6].value, matrix[3][7].value, matrix[3][8].value,
				matrix[4][6].value, matrix[4][7].value, matrix[4][8].value,
				matrix[5][6].value, matrix[5][7].value, matrix[5][8].value,]
	block[6] = [matrix[6][0].value, matrix[6][1].value, matrix[6][2].value,
				matrix[7][0].value, matrix[7][1].value, matrix[7][2].value,
				matrix[8][0].value, matrix[8][1].value, matrix[8][2].value,]
	block[7] = [matrix[6][3].value, matrix[6][4].value, matrix[6][5].value,
				matrix[7][3].value, matrix[7][4].value, matrix[7][5].value,
				matrix[8][3].value, matrix[8][4].value, matrix[8][5].value,]
	block[8] = [matrix[6][6].value, matrix[6][7].value, matrix[6][8].value,
				matrix[7][6].value, matrix[7][7].value, matrix[7][8].value,
				matrix[8][6].value, matrix[8][7].value, matrix[8][8].value,]
	for r in rows:
		for n in range(1, h + 1):
			if {n} not in r:
				return False

	for c in cols:
		for n in range(1, h + 1):
			if {n} not in c:
				return False

	for b in block:
		for n in range(1, h + 1):
			if {n} not in b:
				return False

	return True
def fillInEasies(matrix):
	for r in range(h):
		for c in range(h):
			if len(matrix[r][c].value) > 1:

				for col in range(h):
					if len(matrix[r][col].value) == 1 and col != c:
						matrix[r][c].value -= matrix[r][col].value
						if len(matrix[r][c].value) == 1:
							fillInEasies(matrix)

				for row in range(h):
					if len(matrix[row][c].value) == 1 and row != r:
						matrix[r][c].value -= matrix[row][c].value
						if len(matrix[r][c].value) == 1:
							fillInEasies(matrix)

				blockNum = matrix[r][c].block
				for row in range(h):
					for col in range(h):
						if matrix[row][col].block == blockNum and len(matrix[row][col].value) == 1 and not(r == row and c == col):
							matrix[r][c].value -= matrix[row][col].value
							if len(matrix[r][c].value) == 1:
								fillInEasies(matrix)
	return matrix

def coordinatesOfCellWithMinOptions(matrix):
	smallestValueSet = h
	row = 0
	col = 0
	for r in range(h):
		for c in range (h):
			if(len(matrix[r][c].value) > 1) and (len(matrix[r][c].value) < smallestValueSet):
				row = r
				col = c
				smallestValueSet = len(matrix[r][c].value)
	return row, col

main()
print('	 %5.2f'%(clock()-START_TIME),'sec')
