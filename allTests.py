# IMPORT MODULES
import numpy as np
from ZValues import randNumGenerator

# PARAMETERS
n = 40
SEED = 1505009
k = 9
ZU = randNumGenerator(SEED, n)
###################################################
# UNIFORMITY TEST
# TASKS:
# 01 DIVIDE into k sub-Intervals [DONE]
# 02 Frequency of Ui in that sub interval [DONE]
# 03 Calculate Kai Square [DONE]
###################################################
Us = ZU[1]
print("ALL U's:")
print(Us)
print("maxVal:")
print(max(Us))
print("minVal:")
print(min(Us))

# FIND ALL THE SUB INTERVALS

intervals = np.linspace(0, 1, k, endpoint=False)
intervals = np.append(intervals, [1])

frequencyCount ={}
for i in intervals:
    # print(i)
    frequencyCount[i] = 0

for u in Us:
    print("WORKING U",u)
    for i in range(k+1):
        if u <= intervals[i]:
            frequencyCount[intervals[i-1]] += 1
            print(u,"Done")
            break

print(frequencyCount)


kai_square = 0
kai_sum = 0

for x in frequencyCount.keys():
    kai_sum += (frequencyCount[x] - n/k) ** 2

kai_square = kai_sum*k/n

print(kai_square)

# NEED TO WORK ON THE STUB CODE


# summer = 0
# for x in frequencyCount.keys():
#     summer += frequencyCount[x]
#
# print(summer)

def find_range(number,intervals):
    for i in intervals:
        if number < i:
            return i


#########################################################
# def generate_experiment_probability(x_theory, y_theory, N):
# observation = {}
# for i in Us:
#     observation[i] = 0
#
# for _ in range(0, N - 1):
#     # value = random.randint(0, N) / N
#     for i in Us:
#         if (y_theory[i] >= value) and (i != 0):
#             observation[i] += 1
#             break
# print(observation)
# y_exp = []
# for keys in observation.items():
#     y_exp.append(keys[1] / N)
# # return y_exp
#
#


###################################################
# SERIAL TEST
# TASKS:
# 01 DIVIDE into l = [n/d] Tuples
# 02 Frequency of Ui in that sub interval
# 03 Calculate Kai Square
###################################################

# Us = ZU[1]
# print("ALL U's:")
# print(Us)
# print("maxVal:")
# print(max(Us))
# print("minVal:")
# print(min(Us))

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
# 03 CALCULATE CCapitalR
# 04 Compare with KAI-SQUARE
###################################################

# = [[4529.4, 9044.9, 13568, 18091, 22615, 27892],[]]

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

print(runLength)
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


# Driver program
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

print(runLength)

r = []
for i in range(1, 6 + 1):
    if i not in runLength.keys():
        r.append(0)
    else:
        r.append(runLength[i])

print(len(aMatrix))
print(len(bMatrix))
print(len(r))

# CALCULATE THE R
capitalR = 0
for i in range(0, 6):
    for j in range(0, 6):
        # SUM OF ALL THE PRODUCTS
        capitalR += aMatrix[i][j] * (r[i] - n * bMatrix[i]) * (r[j] - n * bMatrix[j])

# DIVIDE BY n
capitalR /= n
print(capitalR)

# #######################
# COMPARE WITH KAI-SQUARE
# #######################


