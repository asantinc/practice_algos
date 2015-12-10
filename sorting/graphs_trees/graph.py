from collections import defaultdict
import pdb
from ..queues_stacks import queue_with_stacks as queue
from ..queues_stacks.min_stack import PriorityNode 


class Graph(object):
    def __init__(self):
        #access dict with node
        #the node's it points to can also be accessed in O(1) thanks to set access
        self.array = defaultdict(set)


    def add_node(self, data):
        self.array[data] 


    def add_edge(self, origin, dest, directed=True):
        self.array[origin].add(dest)
        if not directed:
            #add it in both directions
            self.array[dest].add(origin)


    def remove(self, node):
        #remove the entry of this node
        del self.array[node]
        #remove it from all other nodes
        for origin, dest_set in self.array.iteritems():
            if node in dest_set:
                self.array[origin].remove(node)
        
    def find_path(self, source, target):
        visited = defaultdict(int)
        q = queue.Queue()
        q.enqueue(node=source)
        while not q.is_empty():
            source = q.dequeue()
            destinations = self.array[source]
            for dest in destinations:
                if dest not in visited:
                    visited[dest]
                    if dest == target:
                        return True
                    else:
                        q.enqueue(node=dest)
        return False

    def __str__(self):
        all_items = list()
        for origin, destinations in self.array.iteritems():
            origin_string = '{} --> '.format(origin.v)
            dest_string = ', '.join([dest.v for dest in destinations])
            all_items.append(origin_string+dest_string)
        return '\n'.join(all_items)

if __name__ == '__main__':
    graph = Graph()
    mirentxu = PriorityNode('Mirentxu')
    graph.add_node(mirentxu)
    valentin = PriorityNode('Valentin')
    graph.add_node(valentin)
    aran = PriorityNode('Arantza')
    graph.add_node(aran)
    graph.add_edge(mirentxu, aran)
    graph.add_edge(valentin, aran)

    enrique = PriorityNode('Enrique')
    graph.add_node(enrique)
    clara = PriorityNode('clara')
    graph.add_edge(enrique, clara)
    graph.add_edge(aran, clara)

    graph.add_node(clara)
    angela = PriorityNode('angela')
    graph.add_node(angela)
    print graph
    print graph.find_path(mirentxu, clara)  
    print graph.find_path(angela, clara)  
    print graph.find_path(enrique, valentin)  

    
    graph.add_edge(angela, mirentxu)
    print graph
    print graph.find_path(mirentxu, clara)  
    print graph.find_path(enrique, mirentxu)  
