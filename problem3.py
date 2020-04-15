if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sum_of_scores = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    maths,physics,chemistry = student_marks[query_name]
    sum_of_scores = maths + physics + chemistry
    average = sum_of_scores/3
    print(type(average))

