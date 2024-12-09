def countingSort(arr):
    lista = [0] * 100
    for i in arr:
        lista[i] += 1
    print("\n\n")
    print(" ".join(map(str, lista)))

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
