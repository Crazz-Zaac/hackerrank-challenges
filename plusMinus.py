
'''
Given an array of integers, calculate the ratios of its elements that are positive, 
negative, and zero. Print the decimal value of each fraction on a new line with  
places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six 
decimal places, though answers with absolute error of up to  are acceptable.

Example:

There are  elements, two positive, two negative and one zero. Their ratios are ,  and .
Results are printed as:

0.400000
0.400000
0.200000

Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be 
printed on a separate line with  digits after the decimal. The function should not return 
a value.

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .
'''

### Solution ###
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    number = [len([n for n in arr if n>0]), len([n for n in arr if n<0]), len([n for n in arr if n==0])]  
    
    for val in number:
        if val != 0:
            print(format(val/len(arr), '.6f'))
        else:
            print(format(0, '.6f'))
        

if __name__ == '__main__':
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
