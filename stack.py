s=[]
for i in range(5):
    l=int(input())
    if(l==1):
        a=int(input())
        if(len(s)!=5):
            s.append(a)
        else:
            print("Overflow: when stack is full")
    elif(l==2):
        if(len(s)!=0):
            s.pop()
        
        else:
            print("Underflow: when there are no elements in the stack and pop operation is performed")
        
    elif(l==3):
        for i in range(len(s)-1,-1,-1):
            print(s[i])
    else:
        pass
