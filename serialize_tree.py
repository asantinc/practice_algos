from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        q.appendleft((root, 0))
        curr_id = 0
        serial_tree = list()
        i = 0
        while q:
            curr_node, curr_id = q.pop()
            print curr_id
            while curr_id > i:
                serial_tree.append('null')
                i+= 1

            serial_tree.append(str(curr_node.val))

            if curr_node.left:
                q.appendleft((curr_node.left, 2*curr_id+1))
                print 'left {}'.format(curr_node.left.val)
            if curr_node.right:
                q.appendleft((curr_node.right, 2*curr_id+2))
                print 'right {}'.format(curr_node.right.val)
                print 'parent {}'.format(curr_node.val)
            i += 1

        return " ".join(serial_tree)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data:
            data = data.split(',')

            curr_node, curr_id = TreeNode(data[0][1:]), 0
            if len(data)>1: #remove the parenthesis
                data[len(data)-1] = data[len(data)-1][:-1]

            print curr_node.val, curr_id
            dummy = TreeNode(0)
            dummy.right = curr_node
            q = deque()
            q.appendleft((curr_node, curr_id))
            while q:
                curr_node, curr_id = q.pop()

                for i in range(1,3):
                    try:
                        index = 2*curr_id+i
                        val = int(float(data[index]))

                        child = TreeNode(val)
                        if i == 1:
                            curr_node.left = child
                        else:
                            curr_node.right = child
                        q.appendleft((child, index))
                    except (ValueError,IndexError) as e:
                        pass

            return dummy.right
        else:
            return None

        
if __name__ == '__main__':
    input = '[0,1, 2, 3, 3, null, 4, 5, 6]'
    codec = Codec()
    root = codec.deserialize(input)
    print codec.serialize(root)


