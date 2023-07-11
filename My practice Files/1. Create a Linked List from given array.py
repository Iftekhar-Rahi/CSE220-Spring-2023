import numpy as np
arr=np.array([0,1,2,3,4,5,6,7,8,9])
class Node:
    def __init__(self,value,location):
        self.value=value
        self.next=location
# head=Node(arr[0])
# tail=head
# i=1
# while i<len(arr):
#     x=Node(arr[i])
#     tail.next=x
#     tail=x
#     i+=1

class LinkedList:
    def __init__(self,arr):
        self.head=Node(arr[0],None)
        self.tail=self.head
        for i in range(1,len(arr)):
            x=Node(arr[i],None)
            self.tail.next=x
            self.tail=x
    def printlinkedlist(self):
        temp = self.head
        while temp!= None:
            print(temp.value, end=" ")
            temp = temp.next

    def printLinkedList(self):
        temp = self.head
        while temp != None:
            if temp.next != None:
                print(temp.value, end='-->')
            else:
                print(temp.value)
            temp = temp.next

    def countNodes(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def nodeAt(self, idx):
        temp = self.head
        count = 0
        while temp != 0:
            if idx == count:
                return temp.value
            temp = temp.next
            count+=1
rahi=LinkedList(arr)
rahi.printLinkedList()
print(rahi.countNodes())
print(rahi.nodeAt(8))