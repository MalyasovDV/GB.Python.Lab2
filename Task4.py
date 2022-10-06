def create_list(n):
    list = []
    for i in range(-n, n + 1):
        list.append(i)
    return list


def show_positions():
    print("Позиции: ")
    with open('positions.txt') as f:
        for line in f:
            print(int(line))


def multiplicate_positions(list):
    result = 1
    with open('positions.txt') as f:
        for line in f:
            result *= list[int(line)]
    return result


print("Введите число N")
n = int(input())

list = create_list(n)
print("Список:", list)

show_positions()

print("Результат перемножения:", multiplicate_positions(list))
