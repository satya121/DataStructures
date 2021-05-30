l=[4,3,7,9,2,1,10,6]
out=[-1]
st=[l[-1]]
for i in range(len(l)-2,-1,-1):
    if(len(st)!=0 and l[i]>=st[-1]):
        st.pop()
    if(len(st)==0):
        out.append(-1)
    else:
        out.append(st[-1])
    st.append(l[i])
print(out[::-1])




