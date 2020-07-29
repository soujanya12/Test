import os
import math
import random
import re
import sys
def findNumber(arr, k):
        res = ""
        if k in arr:
            res = "YES"
        else:
            res = "NO"
        return res
if __name__ == '__main__':
          fptr = open(os.environ.get('OUTPUT_PATH',r"C:\Users\Sgangula2\practise"),'w')
          arr_count = int(input().strip())
          arr = []
          for _ in range(arr_count):
             arr_item = int(input().strip())
             arr.append(arr_item)
          k=int(input().strip())
          res = findNumber(arr,k)
          fptr.write(res + '\n')
          fptr.close()
arr = [5,1,2,3,4]
k=1
print(findNumber(arr,k))