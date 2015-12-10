from binary_search_recursive import binary_search


def find_item_rotated_array(rotated_array, low=0, high=None):
	'''
	The array has an inflection point
	[4,4,5,5,6,7,8,1,1,2,3]
	'''
	high = high if high is not None else len(rotated_array)
	mid = (low+high)/2

	while low<high:
		if rotated_array[mid] > item:
			low = low
			high = mid
			zreturn find_item_rotated_array(rotated_array, low, high)

		elif rotated_array[mid] < item:
			low = mid
			high = high
			return find_item_rotated_array(rotated_array, low, high)

		else:
			return mid