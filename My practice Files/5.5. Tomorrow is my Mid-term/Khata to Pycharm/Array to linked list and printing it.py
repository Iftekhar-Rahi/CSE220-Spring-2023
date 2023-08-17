import numpy as np
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

    def length(self):
        count=0
        temp=self.head
        while temp!=None:
            count+=1
            temp=temp.next
        return count

    def nodeAt(self,index):
        count=0
        temp=self.head
        while temp is not None:
            if count==index:
                return temp
            count+=1
            temp=temp.next
    def indexing(self,value):
        count=0
        temp=self.head
        while temp!=None:
            if temp.value==value:
                return count
            count+=1
            temp=temp.next
        return -1

    def insert(self,value,index):
        if index==0:
            new=Node(value)
            self.head=new
        elif 0<=index<self.length():
            new=Node(value)
            target=self.nodeAt(index-1)
            # print(target.value)
            temp=target.next
            new.next=temp
            target.next=new
    def deleting_odd(self):
        temp=self.head.next
        while temp!=None:
            if temp.value%2==0:
                pass
            else:
                inx=self.indexing(temp.value)
                target=self.nodeAt(inx)
                target.next=target.next.next
            temp = temp.next
        return temp
arr=np.array([1,2,3,4,5,6])
rahi=LinkedList(arr)
rahi.create_LL(arr)
print(rahi.deleting_odd())
rahi.print_LL()
# print(rahi.length())
# print(rahi.nodeAt(5))
# print(rahi.indexing(9))
# rahi.insert(1000,2)
# rahi.print_LL()

