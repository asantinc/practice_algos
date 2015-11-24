#Solve in O(n) running time, O(k) space
'''
Check if two number exist in array where:
abs( num1 - num2) < = t
abs(index_1 - index_2) < = k
'''

def check_dupes_away(array, k=1, t=1):
	def get_bucket_num(num):
		return [(num/t), (num/t)-1, (num/t)+1] if t else [num] 

	buckets = dict()
	delete_q = dict()

	for i, num in enumerate(array):
		curr_buckets = get_bucket_num(num)
		for b in curr_buckets:
			if b in buckets and buckets[b]>= i-k:
				return True
		buckets[curr_buckets[0]] = i

		delete_q[i] = curr_buckets[0]
		if i-k >= 0:
			#only use O(k) space, clean up dict
			to_delete = delete_q[i-k]
			if buckets[to_delete] <= i-k:
				del buckets[to_delete]
			del delete_q[i-k]

		#only to ensure the runtime requirement is met
		assert len(list(buckets.iteritems())) <= k
		assert len(list(delete_q.iteritems())) <= k

	return False


if __name__ == '__main__':
	input = (5, 7, [5000,66000,800,666,77000000, 99999999999, 100000000000000])
	assert False == check_dupes_away(input[2], k=input[0], t=input[1])

	input = (2, 7, [50,66,80,666,77])
	assert True == check_dupes_away(input[2], k=input[0], t=input[1])

	input = (5, 700, [5000,66000,800,666,77000000])
	assert True == check_dupes_away(input[2], k=input[0], t=input[1])

	input = (1, 0, [5000,66000,800,800])
	assert True == check_dupes_away(input[2], k=input[0], t=input[1])


