

class Node:
    def __init__(self, val):
        self.value = val
        self.l_child = None
        self.r_child = None

    def __repr__(self):
        return f"{self.value} --> ({self.l_child}  {self.r_child})"


class BST:
    def insert(self, root, node):
        if root is None:
            return node

        if root.value < node.value:
            root.r_child = self.insert(root.r_child, node)
        else:
            root.l_child = self.insert(root.l_child, node)
        return root

    def in_order(self, root):
        if not root: return None
        else:
            self.in_order(root.l_child)
            print(root.value)
            self.in_order(root.r_child)

    def pre_order(self, root):
        if not root: return None
        else:
            print(root.value)
            self.pre_order(root.l_child)
            self.pre_order(root.r_child)

    def post_order(self, root):
        if not root:
            return None
        else:
            self.post_order(root.l_child)
            self.post_order(root.r_child)
            print(root.value)


root = Node(3)
t = BST()
for i in [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]:
    t.insert(root, Node(i))

t.in_order(root)