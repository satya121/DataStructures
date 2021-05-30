l=list(map(int,input().split()))
s_l=[]
for i in range(len(l)):
    s_l.append(min(l))
    l.remove(min(l))
    
