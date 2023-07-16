import numpy as np
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()

def countNodes(head):
  count = 0
  temp = head
  while temp != None:
    count += 1
    temp = temp.next
  return count

def nodeAt(head, idx):
  temp = head
  for i in range(idx):
    temp = temp.next
    if temp == None:
      break
  return temp
def remove(head,idx):
    if 0<idx<countNodes(head):
        if idx==0:
            head=head.next
        else:
            target=nodeAt(head, idx)
            target.next=target.next.next


def removeAllOdd(head):
    #Write your code here
    temp=head
    tail=head
    count=0
    while temp!=None:
        if temp.elem%2!=0:
            idx=nodeAt(head, count)
            remove(head, idx)
        # elif temp.elem%2==0:
        #     head=temp
        count+=1
        temp = temp.next

    return head
#Tester Code
head = createList(np.array([5,7,6,21,3,62,213,6,121]))
print("Original Input Linked List:")
printLinkedList(head)
#This should print  5-->7-->6-->21-->3-->62-->213-->6-->121

h=removeAllOdd(head)
print("Output Linked List:")
printLinkedList(h)
#This should print  6-->62-->6