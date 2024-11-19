## Opcion ineficiente 

# def aVeryBigSum(ar):
#     suma = 0
#     for i in ar:
#         suma += i
#     return suma
                
# if __name__ == '__main__':
#     ar_count = int(input().strip())
#     ar = list(map(int, input().rstrip().split()))
#     print(aVeryBigSum(ar))


## Opcion mas eficiente
def aVeryBigSum(ar):
    return sum(ar)
                

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(aVeryBigSum(ar))
