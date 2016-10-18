#Sudoku Solver
#
#
#
 # Load the dictionary back from the pickle file.
import pickle
nbrs = pickle.load( open( "sudokuNbrs.pkl", "rb" ) )
from copy import deepcopy
from time import clock
#
h = int(input('please input height: '))
w = int(input('please input width: '))
class GamePiece:
    row = None
    col = None
    nbrs = []
    rowBlock = None
    colBlock = None
    isFixed = False
    value = None
    def __init__(self, rw, cl, nbr):
        GamePiece.row = rw
        GamePiece.col = cl
        GamePiece.rowBlock = int(rw)//(h/3)
        GamePiece.colBlock=int(cl)//(w/3)
    def getCoor():
        return (row, col)
    # def __init__(self, rw, cl, nbr, val):
    #     print('RW: ', rw)
    #     print('CL: ', cl)
    #     print('NBR: ', nbr)
    #     print('VALUE: ', val)
    #     GamePiece.row = rw
    #     GamePiece.col = cl
    #     GamePiece.rowBlock = int(rw)//3
    #     GamePiece.colBlock=int(cl)//3
    #     GamePiece.value = val
    #     GamePiece.isFixed = True
class GameBoard:
    pieces = {}
    nbrs = {}
    unknowns = {}
    def __init__(dic, nbr):
        pieces = dic
        nbrs=nbr
print(nbrs)
#
dic = {}
dic['start']=[]
for key in nbrs:
    dic[key]= GamePiece(key[0], key[1], nbrs[key])
print()
matrix = [[0 for x in range(h)] for x in range(w)]
row=0
col=0
ind = 0
f=open('sudokuMedium.txt','r')
for line in f.readlines():
    ind=0
    col=0
    row=0
    for char in line:
        if char!='\n':
            if col==w:
                col=0
            row=ind//h
            print('INDEX: ',ind, ' CHAR: [', char,']')
            print(row, ', ', col)
            matrix[row][col]=char
            col+=1
            ind+=1
    # print(matrix)
    for x in range(h):
        for y in range(w):
            print (matrix[x][y], end=' ')
        print()
cor = (7,8)
for x in range(h):
    for y in range(w):
        if (x,y) in nbrs[cor]:
            print ('x', end=' ')
        else:
            print('-', end=' ')
    print()
#
def fillInEasies(matrix, h, w):
    for hi in range(3):
        for x in range(h):
            temp = []
            for y in range(w):
                if matrix[x][y]!='.':
                    temp+=[y]
            if len(temp)==(w-1):
                for i in range(w):
                    if str(i+1) not in temp:
                        for y in range(w):
                            if matrix[x][y]=='.':
                                # print('hi')
                                matrix[x][y]=i+1
        for x in range(h):
            temp = []
            for y in range(w):
                if matrix[y][x]!='.':
                    temp+=[y]
            if len(temp)==(w-1):
                for i in range(w):
                    if str(i+1) not in temp:
                        for y in range(w):
                            if matrix[y][x]=='.':
                                # print('hi')
                                matrix[y][x]=i+1
        dicOfPos = {}
        for x in range(h):
            for y in range(w):
                if matrix[x][y]=='.':
                    temp = []
                    dicOfPos[(x,y)]=[]
                    for pos in nbrs[(x,y)]:
                        # print(pos[0],pos[1])
                        if matrix[pos[0]][pos[1]]!='.':
                            temp+=[int(matrix[pos[0]][pos[1]])]
                    print(temp)
                    for i in range(h):
                        if i+1 not in temp:
                            dicOfPos[(x,y)]+=[i+1]
        for key in dicOfPos:
            if len(dicOfPos[key])==1:
                matrix[key[0]][key[1]]=dicOfPos[key][0]
def guess(matrix, h, w):
    dicOfPos = {}
    for x in range(h):
        for y in range(w):
            if matrix[x][y]=='.':
                temp = []
                dicOfPos[(x,y)]=[]
                for pos in nbrs[(x,y)]:
                    print(pos[0],pos[1])
                    if matrix[pos[0]][pos[1]]!='.':
                        temp+=[int(matrix[pos[0]][pos[1]])]
                print(temp)
                for i in range(h):
                    if i+1 not in temp:
                        dicOfPos[(x,y)]+=[i+1]
    n = 0
    for key in dicOfPos:
        n+=len(dicOfPos[key])
    if n==0:
        return 9000
    for key in dicOfPos:
        new = matrix
        if len(dicOfPos[key])!=0:
            new[key[0]][key[1]]=dicOfPos[key][0]
            return new
def isWrong(matrix, h, w):
    temp = []
    for x in range(h):
        for y in range(h):
            if matrix[x][y]=='.':
                return True
            temp+=[int(matrix[x][y])]
        for i in range(h):
            if (i+1) not in temp:
                return True
    for y in range(h):
        for x in range(h):
            temp+=[int(matrix[y][x])]
        for i in range(h):
            if (i+1) not in temp:
                return True
    for x in range(h):
        for y in range(h):
            for nbr in nbrs[(x,y)]:
                if int(matrix[x][y])==int(matrix[nbr[0]][nbr[1]]):
                    return True
    return False
    # print(dicOfPos)
# def isDone(matrix, h, w):
#     for x in range(h):
#         for y in range(h):
#             if matrix[x][y]=='.':
#                 return False
#     for x in range(h):
#         for y in range(h):
#             temp = []
#             temp+=[int(matrix[x][y])]
#             for nbr in nbrs[(x,y)]:
#                 if int(matrix[nbr[0]][nbr[1]]) == int(matrix[x][y]):
#                     return False
#                 temp+=[int(matrix[nbr[0]][nbr[1]])]
#             for i in range(h):
#                 if i+1 not in temp:
#                     return False
#     return True
def recur(matrix, h, w):
    fillInEasies(matrix, h, w)
    if not isWrong(matrix, h, w):
        return matrix
    oldMatrix = deepcopy(matrix)
    matrix = guess(matrix, h, w)
    matrix = recur(matrix, h, w)
    if matrix!=9000:
        if not isWrong(matrix, h, w):
            return matrix
    matrix = restoreValues(matrix, oldMatrix)
    return matrix
fillInEasies(matrix, h, w)
guess(matrix,h,w)
matrix = recur(matrix, h, w)
print(matrix)
# for x in range(h):
#     temp = []
#     for y in range(w):
#         if matrix[y][x]!='.':
#             temp+=[y]
#     if len(temp)==(w-1):
#         for i in range(w):
#             if str(i+1) not in temp:
#                 for y in range(w):
#                     if matrix[y][x]=='.':
#                         # print('hi')
#                         matrix[y][x]=i+1


for x in range(h):
    for y in range(w):
        print (matrix[x][y], end=' ')
    print()
#
#
#
#
#
#
#
#
#
#
#
#
