Z = []
U = []

Z0 = 1009

Z.append(Z0)


def getSquare(num):
    return num * num


def appendZero(num):
    string = str(num)
    while len(string) < 8:
        string = "0" + string

    return string


def findmiddle(string):
    return int(string[2:6])


num = 123456
zeroPadded = appendZero(num)
print(zeroPadded)
print(findmiddle(zeroPadded))


while len(Z) < 100:
    num = Z[-1]
    num = getSquare(num)
    string = appendZero(num)
    zValue = findmiddle(string)
    Z.append(zValue)

print(Z)