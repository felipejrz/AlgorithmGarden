def f(s, q):
    con = 0
    sum = 0
    for i in s[q]:
        sum += i
        con += 1
    return sum / con

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(f(student_marks, query_name)))
