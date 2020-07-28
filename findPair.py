"""find-pair-with-given-sum-array"""
def findpair(arr,arsum):
    output = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] ==  arsum:
                output.append((arr[i],arr[j]))
    return output


arr = [0,1,2,3,4,5,6,7,8,9,0]
arsum=9
print(findpair(arr,arsum))

#output = [(0,9), (1,8), (2,7)...]