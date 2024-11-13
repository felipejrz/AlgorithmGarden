def f(n, arr):
    arr = list(set(arr)) 
    arr.sort(reverse=True) 
    return arr[1]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(f(n, arr))