'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.
'''
import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.low_heap = list()
        self.high_heap = list()
        self.low_num = 0
        self.high_num = 0
        self.median = None

    def push(self, heap, num, count):
        heapq.heappush(heap, num)
        return count+1
    
    def readjust(self, added_num, added_heap, other_num, other_heap):
        if added_num - other_num > 1:
            item = (-1)*heapq.heappop(added_heap)
            heapq.heappush(other_heap, item)
            added_num -= 1
            other_num += 1
        return added_num, added_heap, other_num, other_heap
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.low_num==0 and self.high_num==0:
            heapq.heappush(self.low_heap, -num)
            self.low_num += 1

        else:
            if (-1)*self.low_heap[0] > num:
                self.low_num = self.push(self.low_heap, -num, self.low_num)
                self.low_num, self.low_heap, self.high_num, self.high_heap = self.readjust(self.low_num, 
                                                            self.low_heap, self.high_num, self.high_heap)
            else:
                self.high_num = self.push(self.high_heap, num, self.high_num)
                self.high_num, self.high_heap, self.low_num, self.low_heap = self.readjust(self.high_num, 
                                                            self.high_heap, self.low_num, self.low_heap)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.low_num > self.high_num:
            return (-1)*self.low_heap[0]
        elif self.high_num > self.low_num:
            return self.high_heap[0]
        else:
            return float((-1)*(self.low_heap[0])+self.high_heap[0])/2
            
if __name__ == '__main__':            
    mf = MedianFinder()

    mf.addNum(6)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(10)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(2)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(6)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(5)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(0)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(6)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(3)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(1)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(0)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap

    mf.addNum(0)
    print mf.findMedian()
    print mf.low_heap
    print mf.high_heap





