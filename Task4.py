def create_list(n):
    list = []
    for i in range(-n, n + 1):
        list.append(i)
    return list

n = int(input())
list = create_list(n)
print(list)