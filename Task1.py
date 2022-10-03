def sum_of_digits (floatnum):
    number = str(floatnum)
    sum = 0
    for digit in number:
        if (digit != '.'):
            digit = int(digit)
            sum = digit+sum
    print(floatnum, ": sum of digits is", sum)
    

sum_of_digits(6782)

sum_of_digits(0.56)