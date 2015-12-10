'''
Goal 1:
Check if a binary tree is balanced, where the definition of balanced is that each subtree has 
no more than one less or one more node that the other subtree 

Goal 2:
Given a sorted array, build a BST with minimal height
'''

import pdb

class Tree(object):
    '''
    Recursive tree implementation
    '''
    def __init__(self, data, parent=None):
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent

    def is_root(self):
        if self.parent is None:
            return True
        else:
            return False
    
    def add_right(self, value):
        if self.right is None:
            self.right = Tree(value, self)
            return self.right
        else:
            raise IndexError('Node {} already has a right child'.format(self.data))

    def add_left(self, value):
        if self.left is None:
            self.left = Tree(value, self)
            return self.left
        else:
            raise IndexError('Node {} already has a left child'.format(self.data))


    def is_leaf(self):    
        return self.left is None and self.right is None

    def check_balanced(self):
        '''
        Check if tree is balanced, as described in problem statement above
        '''
        if self.is_leaf() and self.is_root():
            return True
        if self.is_leaf():
            return 1

        num_r, num_l = 0, 0
        if self.left is not None:
            num_l = self.left.check_balanced()
        if self.right is not None:
            num_r = self.right.check_balanced()
        if num_l != -1 and num_r != -1 and (num_l)<= num_r+1 and num_l>=num_r-1:
            if self.is_root():
                return True
            else:
                return num_l+num_r+1
        else:
            return -1 

    @staticmethod
    def build_min_height_bst(sorted_array, low=0, high=None, tree=None):
        if len(sorted_array) == 0:
            return tree
        high = high if high is not None else len(sorted_array)-1

        #find array midpoint
        mid = (low+high)/2
        child_value = sorted_array[mid]
        tree = tree if tree is not None else Tree(child_value)

        if high-low <= 1: #only one element, insert it
            child_value = sorted_array[high]
            child = None
            if child_value < tree.data:
                child = tree.add_left(child_value)
            else:
                child = tree.add_right(child_value)
            #check which child to add to

            if high-low == 1:
                other_child_value = sorted_array[low]
                child.add_left(other_child_value) 
            return tree 

        else:
            child = None
            if child_value < tree.data:
                child = tree.add_left(child_value)
            else:
                child = tree.add_right(child_value)
            #recursive calls
            tree_left = build_min_height_bst(sorted_array, low=low, high=mid-1, tree=child)
            tree_right = build_min_height_bst(sorted_array, low=mid+1, high=high, tree=child)

            child.add_left(tree_left)
            child.add_right(tree_right)

            return child 

       

if __name__ == '__main__':
    tree = Tree('A')
    assert True == tree.check_balanced()

    b = tree.add_left('B')
    assert True == tree.check_balanced()
    c = tree.add_right('C')
    assert True == tree.check_balanced()

    d = b.add_right('D')
    assert True == tree.check_balanced()
    e = b.add_left('E')
    assert -1 == tree.check_balanced()

    f = c.add_right('F')
    assert True == tree.check_balanced()
    g = c.add_left('G')
    assert True == tree.check_balanced()

    o = g.add_right('O')
    p = g.add_left('P')
    assert -1 == tree.check_balanced()


    
    sorted_array = [1,5,8,9,10,15,17]
    Tree.build_min_height_bst(sorted_array, low=0, high=None, tree=None)


