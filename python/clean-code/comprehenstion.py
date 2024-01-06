spam = []
for number in range(10):
    if number % 2 != 0:
        spam.append(str(number))

# better
spam = [str(number) for number in range(10) if number % 2 != 0]

# anoter one
nestedIntList = [[0], [0,1], [0,1,2]]
nestedStrList = []
for sublist in nestedIntList:
    nestedStrList.append([str(i) for i in sublist])