# PARAMETER

TotalRandomNumber = 10


# WORKING CODES

# RANDOM NUMBER GENERATE FUNCTION
def randNumGenerator(seed, n):
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


# CHECKING THE RANDOM NUMBERS
x = randNumGenerator(1505009, 40)
print(x[0])
print(x[1])
print(len(x[0]))
print(len(x[1]))
