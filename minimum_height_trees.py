'''
For a undirected graph with tree characteristics, we can choose any node as the root. 
The result graph is then a rooted tree. Among all possible rooted trees, those with minimum 
height are called minimum height trees (MHTs). Given such a graph, write a function to find 
all the MHTs and return a list of their root labels. 
'''


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
            
        def find_leaves():
            leaves = set()
            seen = set()
            adjacent_edges = collections.defaultdict(set)
            
            for edge in edges:
                for i, node in enumerate(edge):
                    adjacent_edges[node].add(edge[(i+1)%2])
                    
                    if node in seen:
                        if node in leaves:
                            leaves.remove(node)
                    else:
                        seen.add(node)
                        leaves.add(node)
            return leaves, adjacent_edges
        
        leaves, adjacent_edges = find_leaves()

        level = 0
        q = collections.deque()
        for leaf in leaves:
            q.appendleft((leaf, level))

        while q:
            current, level = q.pop()

            for other in adjacent_edges[current]:
                adjacent_edges[other].remove(current)
                if len(adjacent_edges[other]) == 1:
                    q.appendleft((other, level+1))
                    
            if not q:
                roots = sorted([current, prev_node]) if level == prev_level else [current]
                
            prev_node, prev_level = current, level
            
        return roots


