'''
Return all binary tree paths from root to leafs.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        #start at 12:00; end at 12:??
        
        if not root: #root is None
            return []
        q = collections.deque()
        q.appendleft(root)    
        paths = collections.defaultdict(list)
        paths[root].append(str(root.val))
        leaf_paths = list()
        
        while q:
            curr = q.pop()
            
            if curr.left:
                q.appendleft(curr.left)
                paths[curr.left] = copy.copy(paths[curr])
                paths[curr.left].append(str(curr.left.val))
                    
            if curr.right:
                q.appendleft(curr.right)
                paths[curr.right] = copy.copy(paths[curr])
                paths[curr.right].append(str(curr.right.val))
                

            if not curr.left and not curr.right:
                leaf_paths.append('->'.join(paths[curr]))
                            
        return leaf_paths
        
        