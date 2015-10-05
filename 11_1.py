from mergesort import mergesort

def linear_merge(a_original, b):
	'''
	Question 11.1: merge two sorted arrays in increasing order, a and b, 
	where a has enough buffer space to 
	append b.
	'''
	#Need to fake the space
	a = [0]*(len(a_original)+len(b))
	a[:len(a_original)] = a_original

	i = len(a_original)-1
	j = len(b)-1
	k = len(a_original)+len(b)-1
	while i>=0 and j>=0:
		if a[i]>b[j]:
			a[k] = a[i]
			i -= 1
		else:
			a[k] = b[j]
			j -= 1
		k -= 1
	if j > 0:
		a[:k+1] = b[:k+1]
	if j == 0:
		a[0] = b[0]
	return a


if __name__ == '__main__':
	a = [6,5,7,3,4,11,33,9,10]
	b = [-33, 6,9,8,5,-6,19]
	c = [-33, 6,99,8,6,-6]
	d = [0]
	e = []

	a_sorted = mergesort(a)
	b_sorted = mergesort(b)
	c_sorted = mergesort(c)
	d_sorted = mergesort(d)
	e_sorted = mergesort(e)

	print linear_merge(a_sorted, b_sorted)
	print linear_merge(a_sorted, c_sorted)
	print linear_merge(a_sorted, d_sorted)
	print linear_merge(a_sorted, e_sorted)
	print linear_merge(e_sorted, b_sorted)

