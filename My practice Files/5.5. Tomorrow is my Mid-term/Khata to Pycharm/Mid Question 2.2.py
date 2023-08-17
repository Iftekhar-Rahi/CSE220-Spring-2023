import numpy as np
arr=np.array([10,20,30,35,30,45])

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,arr):
        self.head=Node(arr[0])
        self.tail=self.head
    def create_LL(self,arr):
        for i in range(1,len(arr)):
            new_node=Node(arr[i])
            self.tail.next=new_node
            self.tail=new_node

    def print_LL(self):
        temp=self.head
        while temp!=None:
            if temp.next==None:
                print(temp.value)
            else:
                print(temp.value,end="-->")
            temp=temp.next
    def is_sorted_asc(self):
        temp=self.head
        while temp!=None:
            if temp.value<temp.next.value:
                pass
            else:
                return "Not sorted"
            temp=temp.next
        return "Sorted"

rahi=LinkedList(arr)
rahi.create_LL(arr)
rahi.print_LL()
print(rahi.is_sorted_asc())