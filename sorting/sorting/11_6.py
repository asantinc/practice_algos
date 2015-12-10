import pdb
from binary_search import binary_search_recursive

'''
Find an element in a matrix, where each of its rows
and columns are non-decreasing
'''

def diag_mid(low, high):
    #find the mid diagonal point
    min_dim = min(high[0]-low[0], high[1]-low[1])
    x_remains = high[0]-(low[0]+min_dim) 
    y_remains = high[1]-(low[1]+min_dim)

    mid = (low[0]+(min_dim/2), low[1]+(min_dim/2))
    return mid, x_remains, y_remains


def print_array(array, low, high):
    print '*** ARRAY***'
    for x in range(low[0], high[0]+1):
        row = list()
        for y in range(low[1], high[1]+1):
            row.append(array[x][y])
        print ' '.join([str(r) for r in row])


def sort_matrix(item, matrix, low=(0,0), high=None):
    high = (len(matrix)-1, len(matrix[0])-1) if high is None else high
    mid, x_remains, y_remains = diag_mid(low, high)

    if item == matrix[mid[0]][mid[1]]:
        return mid
    elif low==high:
        return -1
    elif low[0]==high[0]:
        #we have a single row or column
        index = binary_search_recursive(matrix[low[0]], item, low=low[1], high=high[1])
        if index != -1:
            return (low[0], index)  
        else:
            return index
    elif low[1] == high[1]:
        #we will need to copy the array over by slicing - no longer O(logn) for this part
        new_array = list()
        for i in range(low[0], high[0]):
            new_array.append(matrix[i][low[1]])

        index = binary_search_recursive(new_array, item)
        if index != -1:
            return (low[0]+index,index[1])
        else:
            return index

    if item < matrix[mid[0]][mid[1]]:
        index = sort_matrix(item, matrix, low, mid)
        if index == -1: #and x_remains: 
            index = sort_matrix(item, matrix, low=(mid[0], low[1]), high=(high[0], mid[1])) 
        
        if index == -1: #and y_remains:
            index = sort_matrix(item, matrix, low=(low[0], mid[1]) , high=(mid[0],high[1])) 

    elif item > matrix[mid[0]][mid[1]]:
        if mid == low:
            mid = high

        index = sort_matrix(item, matrix, mid, high)
        if index == -1: #and x_remains: 
            index = sort_matrix(item, matrix, low=(mid[0], low[1]), high=(high[0], mid[1])) 
        
        if index == -1: #and y_remains:
            index = sort_matrix(item, matrix, low=(low[0], mid[1]) , high=(mid[0],high[1]))

    else: #item found
        return mid

    return index


if __name__ == '__main__':
    matrix = [range(6), range(1, 7), range(2,8), range(3,9)]
    for m, col in enumerate(matrix):
        for i, j in zip(range(6), col):
            matrix[m][i] = j*i
    matrix[3][5] =99 
    matrix[0][0]=-10
    matrix[0][1] = -5

    assert (3,5) == sort_matrix(99, matrix)
    assert (0,1) ==  sort_matrix(-5, matrix)
    assert (2,4) == sort_matrix(24, matrix)
    assert (1,3) == sort_matrix(12, matrix)
    assert (0,5) == sort_matrix(25, matrix)


    matrix.append(range(4,10))
    for m, col in enumerate(matrix):
        if m < 3:
            continue
        for i, j in zip(range(6), col):
            matrix[m][i] = j*i

    assert (0,1) == sort_matrix(-5, matrix)
    assert (2,4) == sort_matrix(24, matrix)
    assert (0,5) == sort_matrix(25, matrix)
    assert (2,2) == sort_matrix(8, matrix)
    assert (3,4) == sort_matrix(112, matrix)



