def mergesort(l,low,mid,high):
    left=low
    right=mid+1
    tmp=[]
    while(left<=mid and right<=high):
        if(l[left]<=l[right]):
            tmp.append(l[left])
            left+=1
        else:
            tmp.append(l[right])
            right+=1
    while(left<=mid):
        tmp.append(l[left])
        left+=1
    while(right<=high):
        tmp.append(l[right])
        right+=1
    for i in range(low,high+1):
        l[i]=tmp[i-low]
    return l
def merge(l,low,high):
    if(low>=high):
        return 0
    mid=(low+high)//2
    merge(l,low,mid)
    merge(l,mid+1,high)
    l=mergesort(l,low,mid,high)
    return l
l=list(map(int,input().split()))
print(l)
l=merge(l,0,len(l)-1)
print(l)
