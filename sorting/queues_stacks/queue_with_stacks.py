'''
Implementation of a queue using two stacks.
'''

import pdb
from min_stack import Stack

class Queue(object):
    def __init__(self):
        self.stacks = [Stack(), Stack()]
        self.enqueue_order = 1 

    def enqueue(self, value=None, node=None, priority=None):
        if not self.enqueue_order:
            self.__reverse()
        if node is None:
            self.stacks[self.enqueue_order].push(value, priority=priority)   
        else:
            self.stacks[self.enqueue_order].push(value=node.v, node=node)   


    def __reverse(self):
        other_index = (self.enqueue_order+1)%2
        while not self.stacks[self.enqueue_order].is_empty():
            item = self.stacks[self.enqueue_order].pop() 
            self.stacks[other_index].push(item.v, node=item)
        self.enqueue_order = other_index 

    def dequeue(self):
        if self.enqueue_order:
            #need to flip it
            self.__reverse()
        return self.stacks[self.enqueue_order].pop()

    def is_empty(self):
        return self.stacks[self.enqueue_order].is_empty()

    def peek(self):
        if not self.is_empty():
            return self.stacks[self.enqueue_order]._Stack__array[0]
        else:
            raise IndexError('The queue is empty, cannot peek')

    def __str__(self):
        items = ['{}'.format(item.v) for item in self.stacks[self.enqueue_order]._Stack__array if item is not None] 
        string_items = '\n'.join(items)
        return string_items
        
    def size(self):
        return self.stacks[self.enqueue_order].size() 
     

if __name__ == '__main__':
    q = Queue()
    values = [1,4,6,7,9,10,22,22,22,30]

    for v in values:
        node = Node(v)
        q.enqueue(node)
    for v in values:
        other = q.dequeue()
        assert other.v == v


