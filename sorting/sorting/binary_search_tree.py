from collections import defaultdict
import Queue
import pdb

'''
Binary search tree with ranking: the find function returns the number 
of existing nodes with values smaller than a given value.
'''

class Node(object):
    def __init__(self, value):
        self.v = value
        self.right = None
        self.left = None

    def is_leaf(self):
        return (self.right is None and self.left is None)


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.ranks = defaultdict(int)

    def insert(self, value, node=None):
        if self.root is None:
            self.root = Node(value)
        else: 
            current = self.root if node is None else node 
            if value < current.v:
                self.ranks[(current, current.v)] += 1
                if current.left is not None:
                    self.insert(value, node=current.left)
                else:
                    current.left = Node(value)
            else:
                if current.right is not None:
                    self.insert(value, node=current.right)
                else:
                    current.right = Node(value)

    def find(self, value):
        rank = 0
        current = self.root
        while not current.is_leaf():
            if value == current.v:
                return True, rank+self.ranks[(current, current.v)]
            elif value < current.v:
                if current.left is not None:
                    current = current.left
                else:
                    return False, -1
            else:
                if current.right is not None:
                    rank += self.ranks[(current, current.v)]+1
                    current = current.right
                else:
                    return False, -1
        if value != current.v:
            return False, -1
        else:
            return True, rank+self.ranks[(current, current.v)]
         

    def get_rank(self, value):
        '''
        Find the number of nodes with values smaller 
        than the given value, if the value is in the BST
        '''
        _, rank = self.find(value)
        return rank
        

    def bfs(self):
        q = Queue.Queue()
        q.put(self.root)

        while not q.empty():
            current = q.get()              
            print current.v
            if current.left is not None:
                q.put(current.left)
                print 'left: {}'.format(current.left.v)
            if current.right is not None:
                q.put(current.right)
                print 'right: {}'.format(current.right.v)

def test_tree(a):
    tree = BinarySearchTree()
    for i in a:
        tree.insert(i)
    for i in a:
        print i, tree.get_rank(i)


if __name__ == '__main__':
    a = [6,8,4,8,9,10,1,3]
    b = [6,6,6]
    c = [8,9,10,1,4,-5,6]
    test_tree(a)
    test_tree(b)
    test_tree(c)

