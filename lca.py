'''
Find lowest common ancestor of a pair of nodes p, q. 
- Do not assume nodes are found in the tree 
- Nodes do not have parent pointers

The second method finds the LCA on a Binary Search
Tree.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node value: {}'.format(self.val)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        if not root or not p or not q:
            return None
        
        parents = {root:None}
        queue = [root]
        self.found_p = False
        self.found_q = False
        
        #BUILD PARENTS DICT
        while queue and (not self.found_p or not self.found_q):
            curr = queue.pop()
            if curr == p:
                self.found_p = True
            if curr == q:
                self.found_q = True
            if curr.left:
                parents[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parents[curr.right] = curr
                queue.append(curr.right)
  
        if not self.found_p or not self.found_q:
            #both nodes not found
            return None
        
        #BACKTRACKING
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            #first node to be in ancestors is shared
            q = parents[q]
        return q


    def lowestCommonAncestorBST(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        if not root or not p or not q:
            return None
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        
        curr = root
        while curr:
            if curr.val>=min_val and curr.val<=max_val:
                return curr
            elif curr.val<min_val and curr.val<max_val:
                curr = curr.right
            elif curr.val>min_val and curr.val>max_val:
                curr = curr.left
                
        return None


if __name__=='__main__':
    root = TreeNode(10)
    a = TreeNode(5)
    b = TreeNode(15)
    c = TreeNode(22)
    d = TreeNode(24)
    e = TreeNode(55)
    f = TreeNode(63)
    g = TreeNode(88)
    h = TreeNode(99)

    root.right = a
    root.left = b
    a.right = c
    a.left = d
    c.left = e
    b.right = f
    d.right = g
    d.left = h

    sol = Solution()
    assert 5 == sol.lowestCommonAncestor(root, d, c).val
    assert 10 == sol.lowestCommonAncestor(root, g, f).val
    assert 10 == sol.lowestCommonAncestor(root, g, b).val
    assert 5 == sol.lowestCommonAncestor(root, e, h).val
