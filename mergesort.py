
import pdb

def merge(array, low, mid, high):
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


a = [6,5,7,3,4,11,33,9,10]
b = [-33, 6,7,8,6,-6,19]
c = [-33, 6,7,8,6,-6]
d = [0]

print mergesort(a)
print mergesort(b)
print mergesort(c)
print mergesort(d)
