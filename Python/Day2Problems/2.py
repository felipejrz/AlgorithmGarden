def diagonalDifference(n, arr):
    sum1, sum2 = 0, 0
    for i in range(n):
        sum1 += arr[i][i]
        sum2 += arr[i][n - 1 - i]
    print (abs(sum1 - sum2))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    diagonalDifference(n, arr)
