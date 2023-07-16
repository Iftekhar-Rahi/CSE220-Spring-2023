class Node:
    def __init__(self,value,):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def nodeAt(self, idx):
        count = 0
        temp = self.head
        while temp != None:
            if count == idx:
                return temp
            count += 1
            temp = temp.next
        return None

    def countNodes(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def append(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            lenth = self.countNodes()
            target = self.nodeAt(lenth - 1)
            target.next = Node(value)
        self.length+=1
    def print(self):
        temp=self.head
        while temp!=None:
            if temp.next!= None:
                print(temp.value, end='-->')
            else:
                print(temp.value)
            temp=temp.next
    def pop(self):
        lenth = self.countNodes()
        if lenth==0:
            self.head=None
        else:
            target = self.nodeAt(lenth - 2)
            target.next = None
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for i in range(self.countNodes()):
            after=temp.next
            temp.next=before
            before=temp
            temp=after




my_linked_list=LinkedList(4)
my_linked_list.append(9)
my_linked_list.append(4)
my_linked_list.append(7)
my_linked_list.append(1)

my_linked_list.pop()
my_linked_list.reverse()
my_linked_list.print()