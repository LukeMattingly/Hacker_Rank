# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:14:01 2019

@author: Kycool13
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourGlasses = 0;
    hgCurrent = -sys.maxsize;
    rows = 0;   
    for h in range(4):
        for i in range(4):
            hgSum = 0     
            for k in range(i,i + 3):
                hgSum += arr[rows][k];  
            hgSum += arr[rows+1][i+1];
            for j in range(i,i + 3):
                hgSum += arr[rows+2][j];
            hourGlasses +=1;
            if(hgCurrent<hgSum):
                hgCurrent=hgSum;
        rows +=1;
        #print("rows", rows)
    return hgCurrent;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
