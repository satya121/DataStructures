'''
BubbleSort: In bubble sort the swapping is done in between two adjacent elements"
'''
class Sorting:
    def __init__(self,data):
        self.data=data
    def Bubble_sort(self):
        for i in range(len(self.data)):
            for j in range(i+1,len(self.data)):
                if(self.data[i]>self.data[j]):
                   self.data[i],self.data[j]=self.data[j],self.data[i]
            print(self.data)
data=list(map(int,input().split()))
obj=Sorting(data)
obj.Bubble_sort()
