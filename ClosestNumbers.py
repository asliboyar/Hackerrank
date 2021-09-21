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
    #first we are sorting the array
    arr.sort()
    #set the minimum difference to a very large number
    mindiff = 10**10
    res = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        #checking if any of the difference is less than the minimum so we can assign the minimum to that value
        if diff < mindiff:
            res = [(arr[i-1], arr[i])]
            mindiff = diff
        elif diff == mindiff:
            res.append((arr[i-1], arr[i]))
    #the res array contains arrays in it so we need to flat the list
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
