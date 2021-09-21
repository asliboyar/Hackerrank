#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    mindiff = 10**10
    res = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        
        if diff < mindiff:
            res = [(arr[i-1], arr[i])]
            mindiff = diff
        elif diff == mindiff:
            res.append((arr[i-1], arr[i]))
    flat_list = []
    for i in res:
        for j in i:
            flat_list.append(j)
    return flat_list
    
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
