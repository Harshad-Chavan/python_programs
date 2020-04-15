"""
Given the names and grades for each student in a Physics class of

students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""


list_student = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
list_marks = [x[1] for x in list_student]
list_marks.sort()
unique = list(dict.fromkeys(list_marks))
second_lowest = unique[1]
list_second_lowest = [x[0] for x in list_student if x[1] == second_lowest]
list_second_lowest.sort()
for studentx in list_second_lowest:
    print(studentx)


