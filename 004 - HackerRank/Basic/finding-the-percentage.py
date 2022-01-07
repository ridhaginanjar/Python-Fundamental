if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    sums = 0
    score_student = student_marks[query_name]
    for i in score_student :
        sums += i
    print("{:.2f}".format(sums/3))