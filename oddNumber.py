import os
def oddNumbers(l,r):
  for num in range(l,r+1):
    if num % 2 != 0:
            yield(num)
if __name__ == '__main__':
        fptr = open(os.environ.get('OUTPUT_PATH', r"C:\Users\Sgangula2\practise\abc.txt"),'w')
        l = int(input().strip())
        r = int(input().strip())
        res = oddNumbers(l,r)
        print(type(res))
        fptr.write('\n'.join(map(str,res)))
        fptr.write('\n')
        fptr.close()
l=2
r=5
print(oddNumbers(l,r))
