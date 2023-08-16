class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
head=Node(11)

a=Node(3)

b=Node(23)

c=Node(7)

d=Node(4)

head.next=a
a.next=b
b.next=c
c.next=d
def print_ll(head):
    tail=head
    while tail!=None:
        if tail.next==None:
            print(tail.value)
        else:
            print(tail.value,end="--> ")
        tail=tail.next
print_ll(head)