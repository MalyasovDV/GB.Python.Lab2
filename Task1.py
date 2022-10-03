def sum_of_digits (floatnum):
    number = str(floatnum)
    sum = 0
    for digit in number:
        if (digit != '.'):
            digit = int(digit)
            sum = digit+sum
    print(sum)
    

def div10(floatnum):
    return floatnum%10

floatnum = 22.85
sum_of_digits(floatnum)
print(div10(floatnum))