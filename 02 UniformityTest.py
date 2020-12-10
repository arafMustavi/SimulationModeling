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