
# attempt 1 (using a list)
def factorial_1(num):
    if num == 0:
        return 1
    numsarray = []
    total = num
    while num > 0:
        num -= 1
        if num == 0:
            break
        numsarray.append(num)
    for i in numsarray:
        total = total * i
    return total

print(factorial_1(6))


# attempt 2(using an other user-defined function)
def sequentialReduction(val):
    return val - 1


def factorial_2(num):
    if num == 0:
        return 1
    multiplier = num
    total = num
    while multiplier > 2:
        multiplier = sequentialReduction(multiplier)
        total = total * multiplier
    return total


print(factorial_2(1))


# attempt 3(no list, no user-defined function)
def factorial_3(num):
    value = 1
    for i in range(2, num+1):
        value *= i
    return value


print(factorial_3(4))


# attempt 4(using recursion) * this is the most optimal method
def factorial_4(num):
    if num == 0:
        return 1
    else:
        return num * factorial_4(num-1) 


print(factorial_4(5))
