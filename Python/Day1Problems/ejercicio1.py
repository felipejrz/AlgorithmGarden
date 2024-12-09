def plusMinus(arr):
    plus, minum, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minum += 1
        else:
            zero += 1
    print(f'{plus/len(arr):.6f}')
    print(f'{minum/len(arr):.6f}')
    print(f'{zero/len(arr):.6f}')
   
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
