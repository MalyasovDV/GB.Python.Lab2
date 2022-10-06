def create_list(n):
    list = []
    for i in range(-n, n + 1):
        list.append(i)
    return list

def multiplicate_positions(list):
    result = 1
    with open('positions.txt') as f:
        for line in f:
            result *= list[int(line)]
    return result

n = int(input())
list = create_list(n)
print(list)
print(multiplicate_positions(list))
