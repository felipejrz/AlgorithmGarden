def findZigZagSequence(a, n):
    a.sort() 
    mid = n // 2 
    
    a[mid], a[n-1] = a[n-1], a[mid]
    
    st = mid + 1
    ed = n - 2
    while st < ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1
    
    print(" ".join(map(int, a)))

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


