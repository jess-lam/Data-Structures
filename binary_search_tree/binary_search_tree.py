"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys

#sys.path.append('/Users/jemlam/Documents/Data-Structures/queue')
from queue import Queue

sys.path.append('../stack/')
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            if self.right.value > self.value:
                return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        
        print(self.value)

        if self.right:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)
        while len(queue) > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

            
        

        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()
        stack.push(self)
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass
        #print is before going left and right
    

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass
        #go left and right first and then print

"""
This code is necessary for testing the `print` methods
"""

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  


