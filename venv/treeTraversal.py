# Tree Traversals (Inorder, Preorder and Postorder)

from functools import cmp_to_key


class Node:

    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)  # return as a string


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

    def create(self, d):  # create binary search tree nodes
        if self.root == None:
            self.root = Node(d)

        else:
            current = self.root

            while 1:
                if d < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(d)
                elif d > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(d)
                else:
                    break

    def preorder(self, node):

        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):

        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def inorder(self, node):

        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)


nodeInfo = [
    [5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]
]

sorted_node = sorted(nodeInfo, key=lambda x: x[1], reverse=True)
print(sorted_node, "\n")

tree = Tree()

for x in sorted_node:
    tree.create(x[0])

print("root\n", tree.root)

tree.preorder(tree.root)
print()
tree.postorder(tree.root)
print()
tree.inorder(tree.root)
print()
