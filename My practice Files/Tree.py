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

def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.elem, end=" --> ")
        in_order(root.right)


def search(root,key):
    if root==None or root.elem==key:
        return root
    else:
        if key<root.elem:
            return search(root.left,key)
        else:
            return search(root.right, key)

def left_most_value(root):
    current=root
    while current.left!=None:
        current=current.left
    return current.elem
def left_most_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_Node(root, key):
    if root is None:
        return root

    if key < root.elem:
        root.left = delete_Node(root.left, key)
    elif key > root.elem:
        root.right = delete_Node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            return temp
        elif root.right is None:
            temp = root.left
            return temp

        temp = left_most_value(root.right)
        root.elem = temp.elem
        root.right = delete_Node(root.right, temp.elem)

    return root

# temp = left_most_value(root.right)
#         root.elem = temp.elem
#         root.right = delete_Node(root.right, temp.elem)

# Driver Code
l1 = [70, 50, 40, 90, 20, 60, 20, 95, 99, 80, 85, 75]
root = Node(l1[0])
for i in l1[1:]:
    addNode(root, i)

# print("Inorder Traversal:")
# in_order(root)
#
# print("\nAdding Node 55:")
# addNode(root, 55)
# in_order(root)
print(left_most_value(root))
root=delete_Node(root,20)
in_order(root)
print()
root=delete_Node(root,100)
in_order(root)
print()
root=delete_Node(root,70)
in_order(root)
