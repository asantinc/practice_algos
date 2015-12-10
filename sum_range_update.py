'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

Example:
Given nums = [1, 3, 5]
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:
    The array is only modifiable by the update function.
    You may assume the number of calls to update and sumRange function is distributed evenly.
'''


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        def makeTree(s_i, e_i, t_i):
            #s_i = start point
            #e_i = end point
            #t_i = level of tree
            st = self.seg_tree
            if s_i == e_i: #single item, leaf
                st[t_i] = nums[s_i]
                return st[t_i]
            mid = s_i + (e_i - s_i) // 2
            #current = left_child+right_child => if not a leaf, then recursion
            st[t_i] = makeTree(s_i, mid, 2 * t_i + 1) + makeTree(mid + 1, e_i, 2 * t_i + 2)
            return st[t_i]

        if nums:
            #tree size = 2*(2^ceil[log(leaves)]) - 1
            tree_length = 2 * (2 ** int(math.ceil(math.log(len(nums), 2)))) - 1
            self.nums = nums
            self.seg_tree = [0] * tree_length
            makeTree(0, len(nums) - 1, 0)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def update_until(s_i, e_i, i, t_i):
            if i > e_i or i < s_i:
                return
            st[t_i] += diff
            if s_i == e_i:
                return
            mid = s_i + (e_i - s_i) // 2
            update_until(s_i, mid, i, 2 * t_i + 1)
            update_until(mid + 1, e_i, i, 2 * t_i + 2)

        st = self.seg_tree
        diff = val - self.nums[i]
        self.nums[i] = val
        update_until(0, len(self.nums) - 1, i, 0)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def sumRange_until(s_i, e_i, t_i):
            if i <= s_i and j >= e_i:
                return st[t_i]
            if s_i > j or e_i < i:
                return 0
            mid = s_i + (e_i - s_i) // 2
            return sumRange_until(s_i, mid, 2 * t_i + 1) + sumRange_until(mid + 1, e_i, 2 * t_i + 2)

        st = self.seg_tree
        if i == j:
            return self.nums[i]

        return sumRange_until(0, len(self.nums) - 1, 0)
