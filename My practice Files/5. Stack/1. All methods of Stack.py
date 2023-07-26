class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,value):
        new=Node(value)
        new.next=self.top
        self.top=new
    def pop(self):
        if self.top==None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
    def size(self):
        count=0
        temp=self.top
        while temp!=None:
            count+=1
            temp=temp.next
        return count
    def isEmpty(self):
        count = 0
        temp = self.top
        while temp != None:
            count += 1
            temp = temp.next

        if count == 0:
            return True
        return False
    def peek(self):
        temp=self.top
        if temp==None:
            return None
        return temp.value
    def printStack(self):
        temp=self.top
        while temp!=None:
            print(f"| {temp.value} |")
            print("|___|")
            temp=temp.next

s=Stack()
s.push(5)
s.push(7)
s.push(5)
s.push(9)
s.printStack()

