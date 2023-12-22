class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = self.right = None

def addNode(root, i):
    if i < root.elem:
        if root.left is None:
            new = Node(i)
            root.left = new
        else:
            addNode(root.left, i)
    elif i > root.elem:
        if root.right is None:
            new = Node(i)
            root.right = new
        else:
            addNode(root.right, i)

def substract(root):
    left=summation(root.left)
    right=summation(root.right)
    return right-left
def summation(root):
    if root==None:
        return 0
    else:
        return root.elem+summation(root.left)+summation(root.right)

def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.elem, end=" --> ")
        in_order(root.right)

# Driver Code
l1 = [70, 50, 40, 90, 20, 60, 95, 99, 80, 85, 75]
root = Node(l1[0])
for i in l1[1:]:
    addNode(root, i)

in_order(root)
print()
print(substract(root))
