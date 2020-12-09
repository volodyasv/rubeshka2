#BinaryTree
class Node():
    value = 0
    left = None
    right = None

    def __init__(self, initialValue):
        self.value = initialValue

    def setRight(self, right):
        self.right = right

    def setLeft(self, left):
        self.left = left

root = Node(50)

newValue = int(input())


if newValue > root.value:
    root.setRight(Node(newValue))
elif newValue < root.value:
    root.setLeft(Node(newValue))
else:
    prinr('Значение уже есть')