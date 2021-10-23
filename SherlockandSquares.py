#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    c = int(math.sqrt(b))-int(math.sqrt(a)) 
    if int(math.sqrt(a))**2==a:
        return c+1 
    else:
         return c
    
  #  for i in range(a, b+1):
   #     if (math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i))):
   #         res += 1
   # return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
