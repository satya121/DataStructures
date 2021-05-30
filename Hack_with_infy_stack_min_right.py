l=list(map(int,input().split()))
st=[l[-1]]
out=[l[-1]]
for i in range(len(l)-2,-1,-1):
    while(len(st)!=0 and l[i]<st[-1]):
        st.pop()
    if(len(st)==0):
        st.append(l[i])
        out.append(l[i])
    else:
        out.append(l[i]-st[-1])
        st.append(l[i])
print(sum(out))
