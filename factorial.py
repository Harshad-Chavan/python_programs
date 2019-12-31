"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

"""
#mysoln
num = int(input("enter a number:"))
if num == 0:
    print(1)
else:
    for m in range(num-1,0,-1):
        num = num * m
    print(num)

