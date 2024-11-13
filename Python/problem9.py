def f(cal):
    score = []
    names = []
    for i in cal:
        score.append(i[1])
    score = list(set(score)) 
    score.sort()
    for i in cal:
        if i[1] == score[1]:
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)

if __name__ == '__main__':
    cal= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        cal.append([name, score])
    f(cal)
        