# IMPORT NECESSARY MODULES
import numpy as np
import math
from ZValues import randNumGenerator
from scipy import stats

# PARAMETERS
n = 10000
k = 9
SEED = 1505009
ZU = randNumGenerator(SEED, n)
Us = ZU[1]
# ALL THE GENERATED VALUES
print("ALL U's:")
print(Us)
print("maxVal:")
print(max(Us))
print("minVal:")
print(min(Us))

###################################################
# TEST 03 RUNS TEST
# TASKS:
# 01 FIND RUN LENGTH
# 02 HARD CODE Aij Bij
# 03 CALCULATE CCapitalR
# 04 Compare with KAI-SQUARE
###################################################
print("\nCURRENT TEST: RUNS TEST\n")

aMatrix = [
    [4529.4, 9044.9, 13568, 18091, 22615, 27892],
    [9044.9, 18097, 27139, 36187, 45234, 55789],
    [13568, 27139, 40721, 54281, 67852, 83685],
    [18091, 36187, 54281, 72414, 90470, 111580],
    [22615, 45234, 67852, 90470, 113262, 139476],
    [278927, 55789, 83685, 111580, 139476, 172860]
]
bMatrix = [1 / 6, 5 / 24, 11 / 120, 19 / 720, 29 / 5040, 1 / 840]

# [51119 291 6 24 120 720 5040 840


testArray = [86, 11, 23, 3, 13, 6, 55, 64, 87, 10]
runLength = {}
# for x in range(len(Us)):
# for x in range(1, len(testArray)):
#     runLength[x] = 0

# print(runLength)
# testArray = [86, 11, 23, 3, 13, 6, 55, 64, 87, 110,121,129,130]
prevIdx = 0
tempLen = 1


# print(testArray)

# FOLLOWING groupSequence CODE WAS MODIFIED FROM GEEKSFORGEEKS
def groupSequence(lst):
    res = [[lst[0]]]

    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            res[-1].append(lst[i])
        else:
            res.append([lst[i]])
    return res


groups = groupSequence(Us)

for x in groups:
    # GET THE LENGTH OF RUN
    tempLen = len(x)
    # CLIP THE LENGTH TO 6
    if tempLen >= 6:
        tempLen = 6
    # INCREASE the RUNLENGTH DICTIONARY FREQUENCY
    if tempLen not in runLength.keys():
        runLength[tempLen] = 0
    runLength[tempLen] += 1

# print(runLength)

r = []
for i in range(1, 6 + 1):
    if i not in runLength.keys():
        r.append(0)
    else:
        r.append(runLength[i])

# print(len(aMatrix))
# print(len(bMatrix))
# print(len(r))

# CALCULATE THE R
capitalR = 0
for i in range(0, 6):
    for j in range(0, 6):
        # SUM OF ALL THE PRODUCTS
        capitalR += aMatrix[i][j] * (r[i] - n * bMatrix[i]) * (r[j] - n * bMatrix[j])

# DIVIDE BY n
capitalR /= n
# print(capitalR)


# ###############################
# ONGOING COMPARE WITH CHI-SQUARE
# ###############################
# PARAMETER
alpha = .10

chi_square_theory = stats.chi2.ppf(df=6, q=1 - alpha)

print("R",capitalR)
print("Chi Square Theory",chi_square_theory)
if capitalR >= chi_square_theory:
    print("RUNS HYPOTHESIS REJECTED")
else:
    print("RUNS HYPOTHESIS ACCEPTED")
##################################################
# RUNS DONE
###################################################
