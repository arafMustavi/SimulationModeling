# PARAMETER

TOTALRANDOMNUMBER = 10
SEED = 1505009

# WORKING CODES

# RANDOM NUMBER GENERATE FUNCTION
def randNumGenerator(seed, n):
    print("Generating total ",n,"Random Numbers for the SEED:",seed)
    # ZvalArray = [1505009]
    # UvalArray = [150509/2**31]

    ZvalArray = []
    UvalArray = []

    ZvalArray.append(seed)
    UvalArray.append(seed / 2 ** 31)

    for i in range(n):
        ZvalArray.append(65539 * ZvalArray[-1] % (2 ** 31))
        UvalArray.append(ZvalArray[-1] / 2 ** 31)

    # print(ZvalArray)
    # print(UvalArray)
    return ZvalArray, UvalArray


# TEST FUNCTION
# CHECKING THE RANDOM NUMBERS
x = randNumGenerator(SEED,TOTALRANDOMNUMBER)
print("TOTAL GENERATED Z:")
print(len(x[0]))
print("TOTAL GENERATED U:")
print(len(x[1]))

print("Z Values:")
print(x[0])
print("U Values:")
print(x[1])

