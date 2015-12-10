# Start 11:55

def ex1():
	n = int((raw_input()))
	output = list()
	for i in range(1, n+1):
		spaces = n-i
		spaces_out = '' if spaces==0 else ''.join([' ']*spaces)
		other_out = ''.join(['#']*i)
		output.append(spaces_out+other_out)

	if output:
		print '\n'.join(output)


def sumOfIntegers(arr):
	return sum(arr)



