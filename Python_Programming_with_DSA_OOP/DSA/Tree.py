# binary tree and breath first search BFS

#from queue import Queue
from StackAndQueue import Queue
from StackAndQueue import Stack
from BinaryTreePrinter import BinaryTreePrinter
class TreeNode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

class BinaryTree:
    def __init__(self):
        self.root=None
    
    
    def insert(self,val):
        if self.root is None:
            self.root=TreeNode(val)
        else:
            nodes=Queue()
            nodes.enqueue(self.root)
            
            while True:
                checking_node=nodes.deque()
                if checking_node.left is None:
                    checking_node.left=TreeNode(val)
                    return
                elif checking_node.right is None:
                    checking_node.right=TreeNode(val)
                    return
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)
                    
    def __str__(self):
            tree_printer = BinaryTreePrinter()
            return tree_printer.get_tree_string(self.root)

    def contains(self, val):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            node = nodes.pop()
            print("Checking node:", node.val)
            if node.val == val:
                return True
            if node.right is not None:
                nodes.push(node.right)
            if node.left is not None:
                nodes.push(node.left)
        return False            
                
# Binary Search Tree Implementation


class BST:
    def __init__(self):
        self.root=None
    
    #recursive tree
    
    def __insert_value(self,node,value):
        if node is None:
            return
        if node.val==value:
            return
        elif value<node.val:
            if node.left is None:
                node.left=TreeNode(value)
                return
            self.__insert_value(node.left,value)
        else:
                if node.right is None:
                    node.right=TreeNode(value)
                    return
                self.__insert_value(node.right,value)
                
            
    
        
    def insert(self,val):
        if self.root is None:
            self.root=TreeNode(val)
            
        else:
            self.__insert_value(self.root,val)
                    
    def __str__(self):
            tree_printer = BinaryTreePrinter()
            return tree_printer.get_tree_string(self.root)
        
    
    # in order traversal L-N-R
    
    def __in_order(self,node):
        if node is None:
            return
        self.__in_order(node.left)
        print (node.val, end=" ")
        self.__in_order(node.right)
        
        
    def in_order(self):
        self.__in_order(self.root)

 # Pre order traversal N-L-R
    
    # def __pre_order(self,node):
    #     if node is None:
    #         return
    #     print (node.val, end=" ")
    #     self.__pre_order(node.left)
        
    #     self.__pre_order(node.right)
        
        
    # def pre_order(self):
    #     self.__pre_order(self.root)
    
# Post order traversal L-R-N
    
    # def __post_order(self,node):
    #     if node is None:
    #         return 
    #     self.__post_order(node.left)
    #     self.__post_order(node.right)
    #     print (node.val, end=" ")
        
        
    # def post_order(self):
    #     self.__post_order(self.root)



# DFS implementation
    def contains(self, val):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            node = nodes.pop()
            print("Checking node:", node.val)
            if node.val == val:
                return True
            elif val < node.val:
                if node.left is not None:
                    nodes.push(node.left)
            else:
                if node.right is not None:
                    nodes.push(node.right) 
        return False

    

bst = BinaryTree()
for i in [8, 2, 1, 10, 100, 50, 40, 23, 16, 7, 9, 200, 150, 300]:
    bst.insert(i)
    print(bst)

#bst.in_order()
print()
print("Contains 10:", bst.contains(10))
print("Contains 9:", bst.contains(9))