# IMPORT NECESSARY MODULES
import numpy as np
import math
from ZValues import randNumGenerator
from scipy import stats

# PARAMETERS
n = 40
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
# TEST 01 UNIFORMITY TEST
# TASKS:
# 01 DIVIDE into k sub-Intervals [DONE]
# 02 Frequency of Ui in that sub interval [DONE]
# 03 Calculate Chi Square [DONE]
###################################################
print("\nCURRENT TEST: UNIFORMITY TEST\n")
# FIND ALL THE SUB INTERVALS
intervals = np.linspace(0, 1, k, endpoint=False)
intervals = np.append(intervals, [1])

frequencyCount = {}
for i in intervals:
    # print(i)
    frequencyCount[i] = 0

for u in Us:
    # print("WORKING U", u)
    for i in range(k + 1):
        if u <= intervals[i]:
            frequencyCount[intervals[i - 1]] += 1
            # print(u, "Done")
            break
# print(frequencyCount)
chi_square = 0
chi_sum = 0
for x in frequencyCount.keys():
    chi_sum += (frequencyCount[x] - n / k) ** 2

chi_square = chi_sum * k / n

# print(chi_square)

###############################
# NEED TO WORK ON THE STUB CODE
###############################
# PARAMETER ALPHA
alpha = 90
chi_square_theory = stats.chi2.ppf(q=k - 1, df=1 - alpha)

if chi_square > chi_square_theory:
    print("UNIFORMITY HYPOTHESIS REJECTED")
else:
    print("UNIFORMITY HYPOTHESIS ACCEPTED")

# summer = 0
# for x in frequencyCount.keys():
#     summer += frequencyCount[x]
#
# print(summer)
# def find_range(number,intervals):
#     for i in intervals:
#         if number < i:
#             return i
# CODE FROM PREVIOUS ASSIGNMENT
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

###################################################
# UNIFORMITY DONE
###################################################
# TEST 02 SERIAL TEST
# TASKS:
# 01 DIVIDE into l = [n/d] Tuples
# 02 Frequency of Ui in that sub interval
# 03 Calculate Kai Square
###################################################
print("\nCURRENT TEST: SERIAL TEST\n")

# FIND ALL THE TUPLES
tupleList = []
# PARAMETERS
d = 3

for i in range(0, len(Us), d):
    temp = tuple(Us[i:i + d])
    tupleList.append(temp)

# print(tupleList)
# print(len(tupleList))
#####################
# TRYING THE SERIALS
#####################
n = 20
k = 8
sum = 0
d = 3
alpha = 0.1
arr = []
l = math.floor(n / d)

dict = {}

for i in range(n // d * d) :
    arr.append(u[i])

    if len(arr) == d:
        pattern = []
        for j in range(d) :
            idx = int(arr[j] * k)
            pattern.append(idx)

        pattern = tuple(pattern)
        if pattern not in dict:
            dict[pattern] = 0

        dict[pattern] += 1
        arr = []

zeros = int(math.pow(k, d) - len(dict))
val = - (l / math.pow(k, d))
val = math.pow(val, 2)
chi_square = val * zeros

for key in dict:
    temp = dict[key] - (l / math.pow(k, d))
    chi_square += math.pow(temp, 2)

chi_square *= (pow(k, d) / l)
y = stats.chi2.ppf(q = 1 - alpha, df = pow(k, d) - 1)

print("Chi_square :", round(chi_square, 3))
print("Analytical Value :", round(y, 3))

if chi_square > y :
    print("HYPOTHESIS REJECTED")
else:
    print("HYPOTHESIS ACCEPTED")
#####################
# SERIALS DONE
#####################
# TEST 03 RUNS TEST
# TASKS:
# 01 FIND RUN LENGTH
# 02 HARD CODE Aij Bij
# 03 CALCULATE CCapitalR
# 04 Compare with KAI-SQUARE
#####################
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
alpha = .90

chi_square_theory = stats.chi2.ppf(q=6, df=1 - alpha)

if capitalR >= chi_square_theory:
    print("RUNS HYPOTHESIS REJECTED")
else:
    print("RUNS HYPOTHESIS ACCEPTED")
##################################################
# RUNS DONE
###################################################
# TEST 04 CORRELATION TEST
# TASKS:
# 01 CALCULATE Aj
# 02 TEST THE NULL HYPOTHESIS
###################################################
print("\nCURRENT TEST: CORRELATION TEST\n")

# ro = {}
# var = {}
A = {}
corparam_j = 3
# for j in range(1000000):
h = math.floor((n - 1) / corparam_j - 1)
sumSum = 0
for k in range(0, h + 1):
    idx1 = 0 + k * corparam_j
    idx2 = 0 + (k + 1) * corparam_j
    product = Us[idx1] * Us[idx2]
    sumSum += product
# ro[j] = (12 / (h + 1)) * sumSum - 3
# var[ro[j]] = (13*h + 7) / ((h+1)**2)
# A[j] = ro[j] / math.sqrt(var[ro[j]])

ro = (12 / (h + 1)) * sumSum - 3
var = (13 * h + 7) / ((h + 1) ** 2)
A[corparam_j] = ro / math.sqrt(var)

# PARAMETER
corparam_alpha = 0.95
z = stats.norm.ppf(1 - corparam_alpha / 2)

if abs(A[corparam_j]) > z:
    print("CORRELATION HYPOTHESIS REJECTED")
else:
    print("CORRELATION HYPOTHESIS ACCEPTED")

################################################
# CORRELATION DONE
###############################################

