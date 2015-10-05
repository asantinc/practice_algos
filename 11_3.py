import pdb

'''
11.3: Given a sorted array of n integers that has been rotated 
an unknown number of times, write code to find an element in 
the array. Assume the array was sorted in increasing order 

Answer: runtime is O(log(n)) is the best case, but it becomes 
O(n) if there are many repeated elements in the array
'''

def binary_search_rotated(item, rotated_list, low=0, high=None):
    high = len(rotated_list)-1 if high is None else high
    mid = (low+high) / 2

    #empty list, or failed search
    if len(rotated_list) == 0 or high < low:
        return -1

    #item has been found
    if rotated_list[mid] == item:
        return mid
    #single item in list
    elif high == low:
        return -1
    
    #search on either half depending on value of the midpoint
    elif rotated_list[mid] > item:
        #search on lower half, or in both if the cut is in the upper half
        index = binary_search_rotated(item, rotated_list, low=low, high=mid)
        if index == -1 and rotated_list[mid] >= rotated_list[high]:
            #don't search in upper half if item already found
            if low == mid:#only two elements int the array
                mid = high
            index = binary_search_rotated(item, rotated_list, low=mid, high=high)
    else:
        if low == mid:#only two elements in the array
            mid = high
        index = binary_search_rotated(item, rotated_list, low=mid, high=high)
        if index == -1 and rotated_list[mid] <= rotated_list[low]:
            #don't search in upper half if item already found
            index = binary_search_rotated(item, rotated_list, low=low, high=mid)            
    return index


if __name__ == '__main__':
    #even number
    rotated_list = [5, 6, 7, 8, 1, 1, 2, 4]
    assert 0 == binary_search_rotated(5, rotated_list) 
    assert 1 == binary_search_rotated(6, rotated_list) 
    assert 2 == binary_search_rotated(7, rotated_list) 
    assert 3 == binary_search_rotated(8, rotated_list) 
    assert 5 == binary_search_rotated(1, rotated_list) 
    assert 6 == binary_search_rotated(2, rotated_list) 
    assert 7 == binary_search_rotated(4, rotated_list) 

    #odd number of elements
    rotated_list = [5, 6, 7, 8, 1]
    assert 0 == binary_search_rotated(5, rotated_list) 
    assert 1 == binary_search_rotated(6, rotated_list) 
    assert 2 == binary_search_rotated(7, rotated_list) 
    assert 3 == binary_search_rotated(8, rotated_list) 
    assert 4 == binary_search_rotated(1, rotated_list) 


    rotated_list = [-5, 6, 7, -1]
    assert 0 == binary_search_rotated(-5, rotated_list) 
    assert 1 == binary_search_rotated(6, rotated_list) 
    assert 3 == binary_search_rotated(-1, rotated_list)
 
    #repeated items
    rotated_list = [4,4,4,4,4,4,4,5,6,8,10,0,1,2]
    assert 11 == binary_search_rotated(0, rotated_list)
    assert len(rotated_list)-1 == binary_search_rotated(2, rotated_list)




