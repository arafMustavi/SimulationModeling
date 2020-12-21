# IMPORT NECESSARY MODULES
import numpy as np
import math
from ZValues import randNumGenerator
from scipy import stats

# PARAMETERS
n = 10000
d = 2
k = 4

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

for i in range(0, len(Us), d):
    temp = tuple(Us[i:i + d])
    tupleList.append(temp)

# print(tupleList)
# print(len(tupleList))
#####################
# TRYING THE SERIALS
#####################
sum = 0
alpha = 0.1
arr = []
l = math.floor(n / d)

dict = {}

for i in range(n // d * d) :
    arr.append(Us[i])

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

print("Chi_square Experiment :", round(chi_square, 3))
print("Analytical Value :", round(y, 3))


if chi_square > y :
    print("HYPOTHESIS REJECTED")
else:
    print("HYPOTHESIS ACCEPTED")

