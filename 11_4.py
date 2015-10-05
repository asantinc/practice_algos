import pdb
'''
11.4: Given a sorted array of strings, interspersed with empty strings, write a method to 
find the location of a given string

Runtime: O(log(n)), in the best case. O(n) if the list contains mostly empty strings.
'''


#do binary search
#if we run into an empty string, keep moving until we find a different item

def modified_binary_search(word, word_list, low=0, high=None):
    high = len(word_list)-1 if high is None else high

    #try to ensure high and low are not empty
    while low<high and word_list[low] == '':
        low += 1
    while high>low and word_list[high] == '':
        high -= 1

    #find the mid element that is not empty
    mid = (low+high)/2
    while mid < high and word_list[mid] == '':
        mid += 1
    if mid == high: #if the upper half is all empty...
        #find a new mid in the lower half
        mid = (low+high)/2 
        while mid > low and word_list[mid] == '':
            mid -= 1
        if mid == low:#the entire sublist if full of empty strings
           if word==word_list[mid]:
               return mid
           elif word==word_list[high]:
               return high
           else:
               return -1  
    
    middle = word_list[mid]
    if word == middle:
        return mid
    if low==high:
        return -1
    if middle != '':
        if middle > word:
            return modified_binary_search(word, word_list, low=low, high=mid)
        else: #middle<word
            return modified_binary_search(word, word_list, low=mid+1, high=high)


if __name__ == '__main__':
    a = ['','']
    assert -1 == modified_binary_search('a', a)

    a = ['aaa','','acv', 'acw', 'bbb', 'bbb','','bbb','','ccc','','','','ddd', '']
    assert 9 == modified_binary_search('ccc', a)

    a = ['','','aaa','bbb']
    assert 3 == modified_binary_search('bbb', a)

    a = ['aaa','','acw', 'bbb', 'bbb','','bbb','','ccc','','','','ddd', '']
    assert 8 == modified_binary_search('ccc', a)

