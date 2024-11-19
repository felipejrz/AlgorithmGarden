def staircase(n):
    for i in range(1, n + 1):
        fila = ' ' * (n - i) + '#' * i
        print(fila)
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
