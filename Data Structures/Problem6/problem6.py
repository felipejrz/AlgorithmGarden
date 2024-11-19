def plusMinus(arr):
    proba = [0,0,0]
    for i in arr:
        if i > 0:
            proba[0] += 1
        elif i < 0:
            proba[1] += 1
        elif i == 0:
            proba[2] += 1
            
    print(f"{proba[0] / len(arr):.6f}")
    print(f"{proba[1] / len(arr):.6f}")
    print(f"{proba[2] / len(arr):.6f}")              

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
