def findMedian(arr):
    suma = sum(arr) / len(arr)
    print(int(suma))   
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
    # fptr.write(str(result) + '\n')
    # fptr.close()
