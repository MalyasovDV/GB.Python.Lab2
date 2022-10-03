import math

def create_list(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.append(round(math.pow(1+1/i, i), 2))
    return sequence

def sum_elements_of_list(sequence):
    sum = 0
    for element in sequence:
        sum += element
    return sum

n = int(input())
list = create_list(n)
print(list)
print(sum_elements_of_list(list))