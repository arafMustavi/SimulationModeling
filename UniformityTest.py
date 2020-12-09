# IMPORT MODULES
import numpy as np
from ZValues import randNumGenerator

# PARAMETERS
n = 40
SEED = 1505009

ZU = randNumGenerator(SEED, n)

# UNIFORMITY TEST
# TASKS:
# 01 DIVIDE into k Subintervals
# 02 Frequency of Ui in that sub interval
# 03 Calculate Kai Square

Us = ZU[1]
print("ALL U's:")
print(Us)
print("maxVal:")
print(max(Us))
print("minVal:")
print(min(Us))

intervals = np.linspace(0,1,10,endpoint=False)
print(intervals)
for i in intervals:
    print(i)




#########################################################
# def generate_experiment_probability(x_theory, y_theory, N):
observation = {}
for i in Us:
    observation[i] = 0

for _ in range(0, N - 1):
    # value = random.randint(0, N) / N
    for i in Us:
        if (y_theory[i] >= value) and (i != 0):
            observation[i] += 1
            break
print(observation)
y_exp = []
for keys in observation.items():
    y_exp.append(keys[1] / N)
# return y_exp

