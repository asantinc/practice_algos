def binary_search_recursive(array, item, low=None, high=None):
	low = low if low is not None else 0
	high = high if high is not None else len(array)
	mid = (low+high)/2

	if low<mid:
		if array[mid] > item:
			return binary_search_recursive(array, item, low=low, high=mid)
		elif array[mid] < item:
			return binary_search_recursive(array, item, low=mid, high=high)
		else:
			return 'Item found at index {}'.format(mid)
	return 'Item not found'


def binary_search_iterative(array, item, low=None, high=None):
	low = 0
	high = len(array)
	mid = (low+high)/2

	while low<mid:
		if array[mid] > item:
			low=low 
			high=mid
		elif array[mid] < item:
			low=mid
			high=high
		else:
			return 'Item found at index {}'.format(mid)
		
		mid = (low+high)/2

	return 'Item not found.'


a = [-2, 4, 5, 5,6, 7]
print binary_search_recursive(a, 6)	
print binary_search_iterative(a, 6)	

b = [-2, 4, 5,6, 7]
print binary_search_recursive(b, 6)	
print binary_search_iterative(b, 6)	
