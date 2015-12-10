'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class CycleDetector(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
            
        p1 = head
        p2 = head
        init = True
        
        while p1 and p2:
            if p1 == p2 and not init:
                break
            init = False
            
            p1 = p1.next
            p2 = p2.next.next if p2.next else None
            
        if not p1 or not p2:
            return None
        
        #look for the start of the cycle
        while head != p2:
            head = head.next
            p2 = p2.next
        return head

if __name__=='__main__':
    head = ListNode(0)
    other_head_pointer = head
    for i in range(1, 10):
        if i == 9:
            head.next = saved_5
        else:
            head.next = ListNode(i)
            if i == 5:
                saved_5 = head.next
            head = head.next

    detector = CycleDetector()
    print detector.detectCycle(other_head_pointer).val

