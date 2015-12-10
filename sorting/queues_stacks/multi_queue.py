from queue_with_stacks import Queue
from min_stack import Node
import pdb

'''
Queue that groups items by class, and keeps track of their insertion order. 
Items are returned in order of overall priority, or if a specific class is requested, 
the item with the highest priority of that class is returned
'''



class MultiQueue(object):
    def __init__(self, multi=2, names=['cat', 'dog']):
        self.queues = dict()
        for name in names:
            self.queues[name] = Queue()
        self.priority = 0
    
    def enqueue(self, v, name):
        self.queues[name].enqueue(v, priority=self.priority)  
        self.priority += 1
    
    def dequeue(self, name=None):
        if name is None:
            min_priority = float('inf')
            for name, q in self.queues.iteritems():
                if not q.is_empty():
                    priority = q.peek().priority
                    if priority < min_priority:
                        min_name = name
                        min_priority = priority
            if min_priority<float('inf'):
                return self.queues[min_name].dequeue(), min_name
            else:
                raise KeyError('Queue is empty.')
        else:
            return self.queues[name].dequeue(), name

    def __str__(self):
        full_string = list()
        for key, q in self.queues.iteritems():
            full_string.append('**{}**\n{}'.format(key, q))
        return '\n'.join(full_string)


if __name__ == '__main__':
    animals = [('cat', 4), ('dog', 6), ('cat', 3), ('cat', 1), ('dog', 2)]
    multi_q = MultiQueue()
    for name, v in animals:
        multi_q.enqueue(v, name)

    for name, v in animals:
        item, n = multi_q.dequeue()
        assert (name, v) == (n, item)


    zoo = [('cat', 4), ('dog', 6), ('cat', 3), ('cat', 55),('cat', 1), ('dog', 2)]
    for name, v in zoo:
        multi_q.enqueue(v, name)

    for name, v in zoo:
        if name == 'cat':
            item, n = multi_q.dequeue(name='cat')
            assert (name, v) == (n, item)

    for name, v in zoo:
        if name == 'dog':
            item, n = multi_q.dequeue(name='dog')
            assert (name, v) == (n, item)

