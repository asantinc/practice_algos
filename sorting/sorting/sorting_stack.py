'''
Sort a stack using only one other an additional stack. This is a version of insertion sort
with runtime of O(n^2).
'''
import pdb

from min_stack import Stack


def sort_stack(stack):
    other_stack = Stack()
    while not stack.is_empty():
        current_v = stack.pop().v
        flip_count = 0
        while not other_stack.is_empty():
            last_value = other_stack.peek()
            if current_v >= last_value: 
                break
            else:
                flip_count += 1
                other_value = other_stack.pop().v
                stack.push(other_value)
        other_stack.push(current_v)
        for i in range(flip_count):
            orig_v = stack.pop().v
            other_stack.push(orig_v)
    return other_stack


if __name__ == '__main__':
    vals = [6,9,10,5,4,7,3,8,22,9]
    stack = Stack()
    for v in vals:
        stack.push(v)
    print vals
    print sort_stack(stack)
