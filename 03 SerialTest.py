# IMPORT MODULES
import numpy as np
from ZValues import randNumGenerator

# PARAMETERS
n = 40
SEED = 1505009
k = 9
ZU = randNumGenerator(SEED, n)
###################################################
# SERIAL TEST
# TASKS:
# 01 DIVIDE into l = [n/d] TUPLES and generate the TUPLES
# 02 Frequency of Ui in that sub interval
# 03 Calculate Kai Square
###################################################
Us = ZU[1]
print("ALL U's:")
print(Us)
print("maxVal:")
print(max(Us))
print("minVal:")
print(min(Us))

# FIND ALL THE TUPLES
# PARAMETERS
d = 3
tupleList = []

for i in range(0, len(Us), d):
    temp = tuple(Us[i:i + d])
    tupleList.append(temp)

print(tupleList)
print(len(tupleList))

###################################################
# RUNS TEST
# TASKS:
# 01 FIND RUN LENGTH
# 02 HARD CODE Aij Bij
# 03
###################################################

    # = [[4529.4, 9044.9, 13568, 18091, 22615, 27892],[]]

aMatrix = [
    [4529.4, 9044.9 , 13568 ,18091 ,22615,27892],
    [9044.9 ,18097 ,27139,36187,45234,55789],
    [13568, 27139,40721,54281,67852,83685],
    [18091 ,36187, 54281 ,72414 , 90470 ,111580],
    [22615, 45234, 67852, 90470, 113262, 139476],
    [278927,55789,83685,111580,139476,172860]
        ]
bMatrix = [1/6,5/24,11/120.19/720.29/5040,1/840]

            # [51119 291 6 24 120 720 5040 840




testArray = [86, 11, 23, 3, 13, 6, 55, 64, 87, 10]
runLength = {}
# for x in range(len(Us)):
# for x in range(1, len(testArray)):
#     runLength[x] = 0

print(runLength)
testArray = [86, 11, 23, 3, 13, 6, 55, 64, 87, 11]
prevIdx = 0
tempLen = 1
print(testArray)

# CODE TAKEN FROM GEEKSFORGEEKS

def groupSequence(lst):
    res = [[lst[0]]]

    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            res[-1].append(lst[i])
        else:
            res.append([lst[i]])
    return res


# Driver program

groups = groupSequence(testArray)

for x in groups:
    tempLen = len(x)
    if tempLen not in runLength.keys():
        runLength[tempLen] = 0
    runLength[tempLen] += 1

print(runLength)