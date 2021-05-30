def selection_sort(l):
    for i in range(len(l)):
        mi=i
        for j in range(i+1,len(l)):
            if(l[mi]>l[j]):
                mi=j
        l[i],l[mi]=l[mi],l[i]
    return l
l=list(map(int,input().split()))
print(selection_sort(l))
