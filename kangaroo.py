#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    curr_pos_x1 = x1
    curr_pos_x2 = x2
    no_of_jumps_x1 = 0
    no_of_jumps_x2 = 0
    if not (x2 > x1 and v2 > v1):
        while curr_pos_x1 != curr_pos_x2:
            curr_pos_x1+=v1
            no_of_jumps_x1+=1
            curr_pos_x2+=v2
            no_of_jumps_x2+=1
            diff = curr_pos_x1 - curr_pos_x2
            if diff == 0:
                break
            print(curr_pos_x1,curr_pos_x2,diff)
            prev_diff = diff
            nxt_diff = (curr_pos_x1+v1) - (curr_pos_x2+v2)
            no_of_jumps_x1+=1
            no_of_jumps_x2+=1
            if nxt_diff == 0:
                break
            if abs(nxt_diff) > abs(prev_diff) or abs(nxt_diff) == abs(prev_diff) :
                return "NO"
        if no_of_jumps_x1 == no_of_jumps_x2:
            return "YES"
        else:
            return "NO"    
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
