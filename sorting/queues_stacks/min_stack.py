import random 
import pdb

'''
Stack implementation that returns the min value of the stack in O(1) time
'''

class IndexError(Exception):
    pass

class Node(object):
    def __init__(self, value, prev=None):
        self.v = value
        self.set_min(prev)

    def set_min(self, prev):
        if prev is not None:
            if self.v < prev.min_val:
                self.min_val = self.v
            else:
                self.min_val = prev.min_val
        else:
            self.min_val = self.v
    

class PriorityNode(Node):
    def __init__(self, v, priority=None, prev=None):
        super(PriorityNode, self).__init__(v, prev=prev)
        self.priority = priority


class Stack(object):
    def __init__(self):
        self.capacity = 100
        self.__array = self.capacity*[None]
        self.head = -1

    def push(self, value, node=None, priority=None):
        #keep track of the minimum in array
        if not self.is_empty():
            prev = self.__array[self.head]
        else:
            prev = None
        if node is None:
            new_node = PriorityNode(value, priority=priority, prev=prev)
        else:
            new_node = node

        #add the new node
        self.head += 1
        if self.head >= self.capacity:
            self.__enlarge() 
        self.__array[self.head] = new_node

    def is_empty(self):
        return not self.head > -1

    def __enlarge(self):
       #double capacity, copy over the items to new array
       self.capacity *= 2
       temp_array = self.capacity*[None]
       temp_array[:len(self.array)] = self.__array[:]
       self.__array = temp_array
    
    def pop(self):
        if not self.is_empty():
            current = self.__array[self.head]
            self.head -= 1
            return current
        else:
            raise IndexError('The stack is empty, could not pop from it')

    def get_min(self):
        if not self.is_empty():
            return self.__array[self.head].min_val
        else:
            raise IndexError('The stack is empty, could not find min')

    def size(self):
        return self.head+1

    def peek(self):
        if not self.is_empty():
            return self.__array[self.head].v
        else:
            raise IndexError('The stack is empty, could not find min')

    def __str__(self):
        items = [str(item.v) for item in self.__array if item is not None] 
        string_items = ', '.join(items)
        return string_items
 

if __name__ == '__main__':
    stack = Stack()
    values = [random.random() for i in range(10)]

    min_list = list()
    for v in values:
        stack.push(v)
        min_list.append(stack.get_min())

    min_list_pop = list()
    for v in values:
        min_list_pop.append(stack.get_min())
        
    min_list_pop = min_list_pop[::-1]
    for i, j in zip(min_list_pop, min_list):
        assert i==j


