import numpy as np
class Node:
  def __init__(self,elem,next = None):
    self.elem, self.next = elem,next


class LinkedList:
    def __init__(self, arr):
        self.head = Node(arr[0])
        tail = self.head
        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            tail.next = newNode
            tail = newNode

    def printLinkedList(self):
        temp = self.head
        while temp != None:
            if temp.next != None:
                print(temp.elem, end='-->')
            else:
                print(temp.elem)
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
        while temp != None:
            if idx == count:
                return temp
            temp = temp.next
            count += 1
        return None

    def elemAt(self, idx):
        temp = self.head
        count = 0
        while temp != None:
            if idx == count:
                return temp.elem
            temp = temp.next
            count += 1
        return f"Invalid index"

    def indexOf(self, value):
        flag = self.head
        count = 0
        while flag != None:
            if flag.elem == value:
                return count
            flag = flag.next
            count += 1
        return f"There is no {value} element in this link list"

    def contains(self, value):
        temp = self.head
        flag = False
        while temp != None:
            if temp.elem == value:
                flag = True
            temp = temp.next
        return flag

    def insert(self, value, idx):  # Done for students
        newNode = Node(value)
        if idx == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            prev = self.nodeAt(idx - 1)
            if prev != None:
                newNode.next = prev.next
                prev.next = newNode

    def remove(self, idx):
        if 0 < idx < self.countNodes():
            if idx == 0:
                self.head = self.head.next
            else:
                target = self.nodeAt(idx - 1)
                target.next = target.next.next

    def rotateRight(self):
        lenth = self.countNodes()
        target = self.nodeAt(lenth - 1)
        target.next = self.head
        self.head = target
        again_target = self.nodeAt(lenth - 1)
        again_target.next = None

    def rotateLeft(self):
        lenth = self.countNodes()
        target = self.nodeAt(lenth - 1)
        target.next = self.head
        self.head = self.head.next
        again_target = self.nodeAt(lenth - 1)
        again_target.next = None


print('Create Linked List')
l1 = LinkedList(np.array([10, 34, 21, 6, -2]))
l1.printLinkedList()
print()

print('Count Nodes of Linked List')
print(l1.countNodes())
print()

print('Find out the node at a certain index')
n = l1.nodeAt(3)
print('Node at index 3:', end=' ')
print(n.elem if n != None else 'Invalid Index')
print('Corner Cases:')
print('Node at index -1:', end=' ')
n = l1.nodeAt(-1)
print(n.elem if n != None else 'Invalid Index')
print('Node at index 5:', end=' ')
n = l1.nodeAt(5)
print(n.elem if n != None else 'Invalid Index')
print()

print('Find out the element at a certain index')
print('Element at index 1:', end=' ')
print(l1.elemAt(1))
print('Corner Cases:')
print('Element at index -2:', end=' ')
print(l1.elemAt(-2))
print('Element at index 6:', end=' ')
print(l1.elemAt(6))
print()

print('Find out the index of an element')
print('Index of element -2', end=' ')
print(l1.indexOf(-2))
print('Corner Cases:')
print('Index of element 23', end=' ')
print(l1.indexOf(23))
print()

print('Find out the if linked list contains an element')
print('Linked List contains -2:', end=' ')
print(l1.contains(-2))
print('Corner Cases:')
print('Linked List contains 3:', end=' ')
print(l1.contains(3))
print()

print('Insert element in certain index')
print('Insert 41 at index 2:', end=' ')
l1.insert(41, 2)
l1.printLinkedList()
print('Corner Cases:')
print('Insert 25 at index 0:', end=' ')
l1.insert(25, 0)
l1.printLinkedList()
print('Insert 15 at index 7:', end=' ')
l1.insert(15, 7)
l1.printLinkedList()
print('Insert 27 at index -1:', end=' ')
l1.insert(27, -1)
l1.printLinkedList()
print()

print('Delete node from a certain index')
print('Delete from index 5:', end=' ')
l1.remove(5)
l1.printLinkedList()
print('Corner Cases:')
print('Delete from index 0:', end=' ')
l1.remove(0)
l1.printLinkedList()
print('Delete from index 5:', end=' ')
l1.remove(5)
l1.printLinkedList()
print('Delete from index -1:', end=' ')
l1.remove(-1)
l1.printLinkedList()
print()

print('Right Rotate')
l1.rotateRight()
l1.printLinkedList()
print()

print('Left Rotate')
l1.rotateLeft()
l1.printLinkedList()
print()