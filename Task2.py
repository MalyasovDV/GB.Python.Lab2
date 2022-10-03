def set_of_multiplications(number):
    multiplications = []
    multiplications.append(1)
    for i in range(2, number + 1):
        multiplications.append(multiplications[i - 2] * i)
    return multiplications


n = 4
print(set_of_multiplications(n))