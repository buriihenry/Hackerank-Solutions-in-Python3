#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

N = int(input())
numbers = list()
counts = list()
for i in range(0,N):
    numbers.append(input())
Q = int(input())
for i in range(0,Q):
    checkstring = input()
    count = 0
    for num in numbers:
        if num == checkstring:
            count = count + 1
    counts.append(count)
for count in counts:
    print(count)