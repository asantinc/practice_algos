
def insertion_sort(array):
	# print 'Time complexity is O(n^2) (remember sum of integers)'
	# print 'Space complexity is O(1)'
	for i, item in enumerate(array):
		if i == 0:
			continue
		j = i-1
		while j>=0 and item<array[j]:
			temp = item
			array[i] = array[j]
			array[j] = temp
			j -= 1
	return array


def bubble_sort(array):
	# print 'Time complexity is O(n^2): at each pass over the array \
	# 		only the last element is guaranteed to be in the correct \
	# 		position.'
	# print 'Space complexity is O(1)'
	swap = True
	for end in range(len(array)-2):
		if swap:
			swap = False
			offset = len(array)-end
			for i, item in enumerate(array[1:offset]):

				if item < array[i]:
					#swap
					swap = True
					temp = array[i]
					array[i] = array[i+1]
					array[i+1] = temp
	return array


def merge(array, low, mid, high):
	# print 'Time complexity is O(n*log(n)): \
	# 				splitting a list of size n takes log(n) time, \
	# 				and sorting each sublist takes O(n) time'
	# print 'Space complexity is O(n)'
	sorted_array = list()

	i = low
	j = mid
	k = 0
	while i < mid and j < high:
		if array[i]<array[j]:
			sorted_array.append(array[i])
			i+=1
		else:
			sorted_array.append(array[j])
			j+=1

	if i < mid:
		sorted_array.extend(array[i:mid])
	elif j < high:
		sorted_array.extend(array[j:high])

	array[low:high] = sorted_array
	return array

def mergesort(array, low=None, high=None):
	if len(array)<2:
		return array
	low = low if low is not None else 0
	high = high if high is not None else len(array)
	mid = ((high+low)/2)

	if (high-low)>2:
		mergesort(array, low, mid)		
		mergesort(array, mid, high)

	#merge the splits
	return merge(array, low, mid, high)


if __name__ == '__main__':
	a = [6,5,7,3,4,11,33,9,10]
	b = [-33, 6,9,8,5,-6,19]
	c = [-33, 6,99,8,6,-6]
	d = [0]
	e = []

	print mergesort(a)
	print mergesort(b)
	print mergesort(c)
	print mergesort(d)
	print mergesort(e)

	print insertion_sort(a)
	print insertion_sort(b)
	print insertion_sort(c)
	print insertion_sort(d)
	print insertion_sort(e)

	print bubble_sort(a)
	print bubble_sort(b)
	print bubble_sort(c)
	print bubble_sort(d)
	print insertion_sort(e)



