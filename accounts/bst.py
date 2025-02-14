# binery Search Tree for searching user acc.

class Node:
    def __init__(self, username):
        self.username = username
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, username):
        if not self.root:
            self.root = Node(username)
        else:
            self._insert(self.root, username)

    def _insert(self, node, username):
        if username < node.username:
            if node.left is None:
                node.left = Node(username)
            else:
                self._insert(node.left, username)
        elif username > node.username:
            if node.right is None:
                node.right = Node(username)
            else:
                self._insert(node.right, username)

    def search(self, username):
        return self._search(self.root, username)

    def _search(self, node, username):
        if node is None:
            return False
        if node.username == username:
            return True
        elif username < node.username:
            return self._search(node.left, username)
        else:
            return self._search(node.right, username)
