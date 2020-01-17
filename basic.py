"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

"""
# str = list(input().split(","))
# print(str)
# print(tuple(str))

""" 
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""
#
# class Basic:
#     def __init__(self):
#         self.str = ""
#         self.getString()
#         self.printstring()
#
#     def getString(self):
#         self.str = self.test()
#
#     def printstring(self):
#         print(self.str.upper())
#
#     def test(self):
#         str = input()
#         return str
#
# b1 = Basic()

"""
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value
(for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 

"""

# import math
# C, H = 50, 30
# D = list(map(int, input().split(",")))
# for _ in D:
#     Q = math.sqrt(((2 * C * _) / H))
#     print(round(Q),end=",")

"""
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the 
array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

"""
# if __name__ == '__main__':
#     X, Y = map(int,input().split(","))
#     main_list = []
#     for i in range(0,X):
#          main_list.append([i*j for j in range(0,Y)])
#     print(main_list)
#

"""
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

# if __name__ == '__main__':
#     words = input().split(",")
#     words.sort()
#     print(",".join(words))


"""
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

# if __name__ == '__main__':
#     lines = []
#     while True:
#         s = input()
#         if s == "":
#             break
#         else:
#             lines.append(s.upper())
#     for sentence in lines:
#         print(sentence)

"""
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

"""

# if __name__ == '__main__':
#     words = input().split()
#     words = list(set(words))
#     words.sort()
#     print(" ".join(words))
#
"""
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
#
# if __name__ == '__main__':
#     numbers = input().split(",")
#     for x in numbers:
#         dec_num = int(x,base=2)
#         if dec_num % 5 == 0:
#             print(x)

"""
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
# if __name__ == '__main__':
#     final_list = []
#     flag = False
#     for x in range(1000, 3001):
#         digits = str(x)
#         for d in digits:
#             if int(d) % 2 == 0:
#                 flag = True
#             else:
#                 flag = False
#         if flag:
#             final_list.append(x)
#     print(final_list)



"""
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
#
# if __name__ == '__main__':
#     sentence = input()
#     letter_count = 0
#     digit_count = 0
#     for alpha in sentence:
#         if alpha.isalpha():
#             letter_count = letter_count + 1
#         elif alpha.isdigit():
#             digit_count = digit_count + 1
#     print("LETTERS {0}".format(letter_count))
#     print("DIGITS {0}".format(digit_count))

"""
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

"""

Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
"""

# if __name__ == '__main__':
#     net_amount = 0
#     while True:
#         s = input()
#         if not s:
#             break
#         trans, amount = s.split()
#         if trans == 'D':
#             net_amount = net_amount + int(amount)
#         elif trans == 'W':
#             net_amount = net_amount - int(amount)
#     print(net_amount)