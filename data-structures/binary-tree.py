class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

class BinarySearchTree:
    def __init__(self, value):
        print 'Root:', value
        self.root = Node(value)

    def add(self, value):
        print 'Adding:', value
        self._insert(self.root, Node(value))
        print self.display()

    def display(self):
        self._display(self.root, 1)

    """
    Prints the tree is a semi-readable form

    Tree:           Becomes:
       10        >   10
      /  \       >     13
     5    13     >       15
         /  \    >       11
       11    15  >     5

    """
    def _display(self, root, level):
        try:
            print '{0}{1}'.format('  '*level, root.data)
        except AttributeError:
            # print '{0}{1}'.format('  '*(level), None)
            return

        self._display(root.right, level + 1)
        self._display(root.left, level + 1)

        return

    def _insert(self, root, node):

        # Right Insert
        if (node.data > root.data):

            # Right position open
            if (root.right is None):
                root.right = node
                return True

            # Right position closed
            else:
                return self._insert(root.right, node)

        # Left Insert
        else:

            # Left position open
            if (root.left is None):
                root.left = node
                return True

            # Left position closed
            else:
                return self._insert(root.left, node)



bst = BinarySearchTree(10)

# bst.display()
bst.add(5)
bst.add(13)
bst.add(15)
bst.add(11)
bst.display()




