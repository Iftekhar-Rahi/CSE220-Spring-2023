class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node

    def push(self,value):
        new=Node(value)
        new.next=self.top
        self.top=new

    def pop(self):
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp.value

    def size(self):
        count=0
        temp=self.top
        while temp!=None:
            count+=1
            temp=temp.next
        return count

    def isEmpty(self):
        elem=self.size()
        if elem==0:
            return True
        return False

    def peek(self):
        temp=self.top
        temp.next=None
        return temp

    def printStack(self):
        temp=self.top
        while temp!=None:
            print(f"| {temp.value} |")
            print("|___|")
            temp=temp.next

s=Stack(1)
