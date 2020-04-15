if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores_temp = student_marks.get(query_name)
    average = float(sum(scores_temp)) / float(len(scores_temp))
    print("%.2f" % average)
