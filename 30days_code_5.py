import math
import os
import random
import re
import sys
n = int(input())
if 2<=n<=20:
    for i in range(1,11):
        result = n*i
        print(n,"x",i,"=",result)
