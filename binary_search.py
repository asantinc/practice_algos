def binary_search(array, item, low=None, high=None):
	low = low if low is not None else 0
	high = high if high is not None else len(array)
	mid = (low+high)/2

	while low<mid:
		if array[mid] > item:
			return binary_search(array, item, low=low, high=mid)
		elif array[mid] < item:
			return binary_search(array, item, low=mid, high=high)
		else:
			return 'Item found at index {}'.format(mid)
	return 'Item not found'


a = [-2, 4, 5, 5,6, 7]
print binary_search(a, 6)	

b = [-2, 4, 5,6, 7]
print binary_search(b, 6)	
