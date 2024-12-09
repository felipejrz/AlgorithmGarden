def flippingMatrix(matrix, col_index):
    print(matrix)
    n = len(matrix)
    for i in range(n // 2):
        matrix[i][col_index], matrix[n - i - 1][col_index] = matrix[n - i - 1][col_index], matrix[i][col_index]
    # for i in matrix:
        # for j in matrix:
            # pass
            # print(matrix[i][j])
    print(matrix)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())
        print(n, end="")
        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix, n)

