# IMPORT NECESSARY MODULES
import numpy as np
import math
from ZValues import randNumGenerator
from scipy import stats

# PARAMETERS
k = 10
n = 10000
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
alpha = 0.1
chi_square_theory = stats.chi2.ppf(df=k - 1, q=1 - alpha)

# y = stats.chi2.ppf(q = 1 - alpha, df = pow(k, d) - 1)

print("K",k)
print("N",n)
print("CHI-SQUARE THEORITICAL :",chi_square_theory)
print("CHI-SQUARE EXPERIMENTAL",chi_square)

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
