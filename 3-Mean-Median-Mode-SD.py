list = [45, 34, 36, 22, 32, 35, 67, 98, 45]

sortedList = sorted(list)
print(sortedList)

n = len(sortedList)

if n % 2 == 0:
    x = (sortedList[n // 2])
    y = (sortedList[n // 2] - 1)
    median = (x + y) / 2
    print('Median:', median)
else:
    median = sortedList[n // 2]
    print('Median: ', median)


# Mode

from collections import Counter

def getMode(list):
    x = {}
    for i in list:
        if not i in x:
            x[i] = 1
        else:
            x[i] += 1
    print('X:',x)
    return [g for g, l in x.items() if l == max(x.values())]

mode = getMode(list)
print(mode)            