#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    count=0
    ma=0
    b=[int(d) for d in str(bin(n))[2:]]
    for i in range (0,len(b)):
        if b[i]==0:
            count=0
        else:
            count+=1
        ma = max(count, ma)
    print(ma)
