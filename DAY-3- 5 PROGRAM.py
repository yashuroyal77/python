def minjumps(arr,l,h):
    if(h==1):
       return 0
    if(arr[l]==0):
       return float('inf')
    min=float('inf')
    for i in range(l+1,h+1):
       if(i<l+arr[l]+1):
          jumps=minjumps(arr,i,h)
          if(jumps!=float('inf')and jumps+1<min):
             min=jumps+1
    return min
arr=[1,3,4,5,6,7,2,5,]
n=len(arr)
print('minimum number of jumps to reach','end is',minjumps(arr,0,n-1))
