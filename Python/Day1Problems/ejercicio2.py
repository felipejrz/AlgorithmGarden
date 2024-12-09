import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    menor = min(arr)
    mayor = max(arr)
    
    suma = sum(arr)
    
    print(f'{suma - mayor} {suma - menor}')
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
