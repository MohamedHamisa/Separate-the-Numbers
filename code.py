#!/bin/python3

import math
import os
import random
import re
import sys


def separateNumbers(s):
    for i in range(len(s)//2):
        a=s[0:i+1]
        b=""
        c=int(a)
        b=b+a
        while True:
            c=c+1
            b=b+str(c)
            if len(b)>=len(s):
                break
        if b==s:
            print("YES",a)
            return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
