def diagonalDifference(arr):
    suma = 0
    suma1 = 0
    for i in range(len(arr)):
        suma += arr[i][i]
        suma1 += arr[i][len(arr)-i-1]
    print(abs(suma1 - suma))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    diagonalDifference(arr)