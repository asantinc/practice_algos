'''
11.7: The goal is to build the tallest possible tower of people standing atop one anothers shoulders, 
with the constraint that every person must be shorter and lighter than the people below them
'''

import random

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
		if array[i].h<array[j].h:
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


class Person(object):
    def __init__(self, height=None, weight=None):
        self.h = height if height is not None else 100*random.random()
        self.w = weight if weight is not None else (5*random.uniform(-1,1))+(self.h)

    def __repr__(self):
        return 'H: {} W: {} \n'.format(self.h, self.w)
    def __str__(self):
        return 'H: {} W: {}'.format(self.h, self.w)



def build_tower(people):
    #O(nlog(n)) if we use mergesort
    #sort people by height
    sorted_people = mergesort(people)

    best_start = best_end = 0
    cur_start = cur_end = 0

    prev_w = None
    for p in sorted_people:
        if prev_w is None or prev_w <= p.w:
            if (cur_end-cur_start) > (best_end-best_start):
                best_start = cur_start
                best_end = cur_end
            cur_end += 1
        else:
            cur_end += 1
            cur_start = cur_end
        prev_w = p.w
    return sorted_people[best_start:best_end]
     


if __name__ == '__main__':
    #get random people
    people = list()
    for p in range(30):
        people.append(Person())
    people_in_tower = build_tower(people)
    print people_in_tower, len(people_in_tower)

