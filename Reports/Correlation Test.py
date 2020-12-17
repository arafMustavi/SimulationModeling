# IMPORT NECESSARY MODULES
import numpy as np
import math
from ZValues import randNumGenerator
from scipy import stats

# PARAMETERS
n = 4000
corparam_j = 1
corparam_alpha = 0.1
# k = 9
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
# TEST 04 CORRELATION TEST
# TASKS:
# 01 CALCULATE Aj
# 02 TEST THE NULL HYPOTHESIS
###################################################
print("\nCURRENT TEST: CORRELATION TEST\n")

# ro = {}
# var = {}
A = {}
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
z = stats.norm.ppf(1 - corparam_alpha / 2)

print("Aj",abs(A[corparam_j]))
print("Z Values",z)
if abs(A[corparam_j]) > z:
    print("CORRELATION HYPOTHESIS REJECTED")
else:
    print("CORRELATION HYPOTHESIS ACCEPTED")

################################################
# CORRELATION DONE
###############################################

